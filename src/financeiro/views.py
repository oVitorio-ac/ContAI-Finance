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

# Configure logger
logger = logging.getLogger("financeiro")

# Add MCP server to path
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
        question = request.POST.get("question", "")
        selected_file = request.POST.get("file", "")
        logger.info(f"POST - Question: '{question}', File: '{selected_file}'")

        try:
            logger.info("Initializing CSVAnalyzer...")
            analyzer = CSVAnalyzer()
            logger.info("CSVAnalyzer initialized")

            if not selected_file:
                response_text = "Please select a CSV file first."
            else:
                question_lower = question.lower()
                if "analysis" in question_lower or "análise" in question_lower:
                    result = analyzer.analyze_csv(selected_file)
                    response_text = _format_analysis_response(result)
                elif "total" in question_lower:
                    result = analyzer.query_data(selected_file, "total")
                    response_text = _format_query_response(result, question)
                elif "average" in question_lower or "média" in question_lower:
                    result = analyzer.query_data(selected_file, "average")
                    response_text = _format_query_response(result, question)
                elif "insights" in question_lower:
                    bedrock = BedrockDataAutomation()
                    file_path = os.path.join("media/uploads", selected_file)
                    result = bedrock.generate_financial_insights(file_path)
                    response_text = _format_insights_response(result)
                else:
                    result = analyzer.query_data(selected_file, question)
                    response_text = _format_query_response(result, question)

        except Exception as e:
            logger.error(f"Error in chat_view: {str(e)}", exc_info=True)
            response_text = f"Error processing request: {str(e)}"

        logger.info(f"Returning response: {response_text[:50]}...")
        return JsonResponse({"response": response_text})

    # GET request - load available files
    logger.info("GET request - loading files")
    try:
        analyzer = CSVAnalyzer()
        files = analyzer.list_csv_files()
        logger.info(f"Files loaded: {len(files)}")
    except Exception as e:
        logger.error(f"Error loading files: {str(e)}", exc_info=True)
        files = []

    return render(request, "chat.html", {"arquivos": files})


def _format_analysis_response(result):
    """Formats CSV analysis response"""
    if "error" in result:
        return f"Error: {result['error']}"

    response = f"📊 Analysis of file {result['filename']}:\n\n"
    response += f"📈 Dimensions: {result['shape']['rows']} rows, {result['shape']['columns']} columns\n"
    response += f"📋 Columns: {', '.join(result['columns'])}\n\n"

    if "value_columns" in result:
        response += "💰 Financial Analysis:\n"
        for col in result["value_columns"]:
            analysis_key = f"{col}_analysis"
            if analysis_key in result:
                data = result[analysis_key]
                response += f"• {col}: Total $ {data['total']:,.2f}, Average $ {data['average']:,.2f}\n"
                response += f"  Positives: {data['positive_count']}, Negatives: {data['negative_count']}\n"

    return response


def _format_query_response(result, question):
    """Formats specific query response"""
    if "error" in result:
        return f"Error: {result['error']}"

    if "message" in result:
        return result["message"]

    response = f"🔍 Results for '{question}':\n\n"

    if "totals" in result:
        response += "📊 Totals:\n"
        for col, value in result["totals"].items():
            response += f"• {col}: $ {value:,.2f}\n"

    elif "averages" in result:
        response += "📊 Averages:\n"
        for col, value in result["averages"].items():
            response += f"• {col}: $ {value:,.2f}\n"

    elif "maximums" in result:
        response += "📊 Maximum Values:\n"
        for col, data in result["maximums"].items():
            response += f"• {col}: $ {data['value']:,.2f} (row {data['row']})\n"

    elif "minimums" in result:
        response += "📊 Minimum Values:\n"
        for col, data in result["minimums"].items():
            response += f"• {col}: $ {data['value']:,.2f} (row {data['row']})\n"

    elif "positive_values" in result:
        response += "📊 Positive Values:\n"
        for col, data in result["positive_values"].items():
            response += (
                f"• {col}: {data['count']} records, Total $ {data['total']:,.2f}\n"
            )

    elif "negative_values" in result:
        response += "📊 Negative Values:\n"
        for col, data in result["negative_values"].items():
            response += (
                f"• {col}: {data['count']} records, Total $ {data['total']:,.2f}\n"
            )

    return response


def _format_bedrock_response(result):
    """Formats Bedrock response"""
    if "error" in result:
        return f"❌ {result['error']}"

    response = "🤖 AI Analysis (AWS Bedrock):\n\n"

    if "analysis" in result:
        response += result["analysis"]

    if "data_summary" in result:
        summary = result["data_summary"]
        response += f"\n\n📊 Data Summary:\n"
        response += f"• {summary['rows']} records\n"
        response += f"• Columns: {', '.join(summary['columns'])}\n"

    return response


def _format_insights_response(result):
    """Formats automatic insights response"""
    if "error" in result:
        return f"❌ {result['error']}"

    response = "💡 Automatic Insights (AWS Bedrock):\n\n"

    if "insights" in result:
        response += result["insights"]

    if "detected_columns" in result:
        cols = result["detected_columns"]
        response += f"\n\n🔍 Detected Columns:\n"
        if cols["values"]:
            response += f"• Values: {', '.join(cols['values'])}\n"
        if cols["dates"]:
            response += f"• Dates: {', '.join(cols['dates'])}\n"

    return response


@csrf_exempt
def test_view(request):
    """Test view to verify if POST works"""
    if request.method == "POST":
        return JsonResponse({"status": "POST working", "data": dict(request.POST)})
    return JsonResponse({"status": "GET working", "method": request.method})
