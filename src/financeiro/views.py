import json
import logging
import os
import sys
from pathlib import Path

import boto3
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import UploadArquivoForm
from .models import UploadArquivo

# Configurar logger
logger = logging.getLogger("financeiro")

# Adiciona o servidor MCP ao path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "mcp_server"))
from bedrock_integration import BedrockDataAutomation
from csv_analyzer import CSVAnalyzer


def upload_view(request):
    """
    View for uploading files. Displays form and processes upload to S3.
    """
    if request.method == "POST":
        form = UploadArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            # Save to model (for now, local; later integrate S3)
            upload = form.save()

            # TODO: Integrate with S3 using boto3
            # Example code (uncomment and configure when S3 is set up):
            # s3_client = boto3.client('s3',
            #                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            #                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            #                          region_name=settings.AWS_S3_REGION_NAME)
            # s3_client.upload_fileobj(upload.arquivo, settings.AWS_STORAGE_BUCKET_NAME, f'uploads/{upload.arquivo.name}')

            return redirect("chat")  # Redirect to chat after successful upload
    else:
        form = UploadArquivoForm()
    return render(request, "upload.html", {"form": form})


@csrf_exempt
def chat_view(request):
    """
    View for chat interface. Renders template and handles POST for questions.
    """
    logger.info(f"Chat view - Method: {request.method}, Path: {request.path}")
    logger.info(f"Headers: {dict(request.headers)}")

    if request.method == "POST":
        pergunta = request.POST.get("pergunta", "")
        arquivo_selecionado = request.POST.get("arquivo", "")
        logger.info(f"POST - Pergunta: '{pergunta}', Arquivo: '{arquivo_selecionado}'")

        try:
            logger.info("Inicializando CSVAnalyzer...")
            analyzer = CSVAnalyzer()
            logger.info("CSVAnalyzer inicializado")

            if not arquivo_selecionado:
                resposta = "Por favor, selecione um arquivo CSV primeiro."
            else:
                if "análise" in pergunta.lower():
                    result = analyzer.analyze_csv(arquivo_selecionado)
                    resposta = _format_analysis_response(result)
                elif "total" in pergunta.lower():
                    result = analyzer.query_data(arquivo_selecionado, "total")
                    resposta = _format_query_response(result, pergunta)
                elif "média" in pergunta.lower():
                    result = analyzer.query_data(arquivo_selecionado, "média")
                    resposta = _format_query_response(result, pergunta)
                elif "insights" in pergunta.lower():
                    bedrock = BedrockDataAutomation()
                    arquivo_path = os.path.join("media/uploads", arquivo_selecionado)
                    result = bedrock.generate_financial_insights(arquivo_path)
                    resposta = _format_insights_response(result)
                else:
                    result = analyzer.query_data(arquivo_selecionado, pergunta)
                    resposta = _format_query_response(result, pergunta)

        except Exception as e:
            logger.error(f"Erro no chat_view: {str(e)}", exc_info=True)
            resposta = f"Erro ao processar: {str(e)}"

        logger.info(f"Retornando resposta: {resposta[:50]}...")
        return JsonResponse({"resposta": resposta})

    # GET request - carrega arquivos disponíveis
    logger.info("GET request - carregando arquivos")
    try:
        analyzer = CSVAnalyzer()
        arquivos = analyzer.list_csv_files()
        logger.info(f"Arquivos carregados: {len(arquivos)}")
    except Exception as e:
        logger.error(f"Erro ao carregar arquivos: {str(e)}", exc_info=True)
        arquivos = []

    return render(request, "chat.html", {"arquivos": arquivos})


def _format_analysis_response(result):
    """Formata resposta de análise do CSV"""
    if "error" in result:
        return f"Erro: {result['error']}"

    response = f"📊 Análise do arquivo {result['filename']}:\n\n"
    response += f"📈 Dimensões: {result['shape']['rows']} linhas, {result['shape']['columns']} colunas\n"
    response += f"📋 Colunas: {', '.join(result['columns'])}\n\n"

    if "value_columns" in result:
        response += "💰 Análise Financeira:\n"
        for col in result["value_columns"]:
            analysis_key = f"{col}_analysis"
            if analysis_key in result:
                data = result[analysis_key]
                response += f"• {col}: Total R$ {data['total']:,.2f}, Média R$ {data['average']:,.2f}\n"
                response += f"  Positivos: {data['positive_count']}, Negativos: {data['negative_count']}\n"

    return response


def _format_query_response(result, pergunta):
    """Formata resposta de consulta específica"""
    if "error" in result:
        return f"Erro: {result['error']}"

    if "message" in result:
        return result["message"]

    response = f"🔍 Resultado para '{pergunta}':\n\n"

    if "totals" in result:
        response += "📊 Totais:\n"
        for col, value in result["totals"].items():
            response += f"• {col}: R$ {value:,.2f}\n"

    elif "averages" in result:
        response += "📊 Médias:\n"
        for col, value in result["averages"].items():
            response += f"• {col}: R$ {value:,.2f}\n"

    elif "maximums" in result:
        response += "📊 Valores Máximos:\n"
        for col, data in result["maximums"].items():
            response += f"• {col}: R$ {data['value']:,.2f} (linha {data['row']})\n"

    elif "minimums" in result:
        response += "📊 Valores Mínimos:\n"
        for col, data in result["minimums"].items():
            response += f"• {col}: R$ {data['value']:,.2f} (linha {data['row']})\n"

    elif "positive_values" in result:
        response += "📊 Valores Positivos:\n"
        for col, data in result["positive_values"].items():
            response += (
                f"• {col}: {data['count']} registros, Total R$ {data['total']:,.2f}\n"
            )

    elif "negative_values" in result:
        response += "📊 Valores Negativos:\n"
        for col, data in result["negative_values"].items():
            response += (
                f"• {col}: {data['count']} registros, Total R$ {data['total']:,.2f}\n"
            )

    return response


def _format_bedrock_response(result):
    """Formata resposta do Bedrock"""
    if "error" in result:
        return f"❌ {result['error']}"

    response = "🤖 Análise com AWS Bedrock:\n\n"

    if "analysis" in result:
        response += result["analysis"]

    if "data_summary" in result:
        summary = result["data_summary"]
        response += f"\n\n📊 Resumo dos dados:\n"
        response += f"• {summary['rows']} registros\n"
        response += f"• Colunas: {', '.join(summary['columns'])}\n"

    return response


def _format_insights_response(result):
    """Formata resposta de insights automáticos"""
    if "error" in result:
        return f"❌ {result['error']}"

    response = "💡 Insights Automáticos (AWS Bedrock):\n\n"

    if "insights" in result:
        response += result["insights"]

    if "detected_columns" in result:
        cols = result["detected_columns"]
        response += f"\n\n🔍 Colunas detectadas:\n"
        if cols["values"]:
            response += f"• Valores: {', '.join(cols['values'])}\n"
        if cols["dates"]:
            response += f"• Datas: {', '.join(cols['dates'])}\n"

    return response


@csrf_exempt
def test_view(request):
    """View de teste para verificar se POST funciona"""
    if request.method == "POST":
        return JsonResponse({"status": "POST funcionando", "data": dict(request.POST)})
    return JsonResponse({"status": "GET funcionando", "method": request.method})
