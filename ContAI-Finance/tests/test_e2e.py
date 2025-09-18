import pytest
import os
import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from financeiro.models import UploadArquivo


@pytest.mark.e2e
class TestFluxoCompleto(TestCase):
    """Testes End-to-End do fluxo completo da aplicação"""
    
    def setUp(self):
        """Setup para cada teste"""
        self.client = Client()
        
        # Criar arquivo CSV de teste
        self.csv_content = b"""data,descricao,valor,categoria
2024-01-01,Receita Vendas,1500.00,Receita
2024-01-02,Despesa Aluguel,-800.00,Despesa
2024-01-03,Receita Servicos,2200.00,Receita
2024-01-04,Despesa Energia,-150.00,Despesa"""
        
        self.arquivo_csv = SimpleUploadedFile(
            "financeiro_teste.csv",
            self.csv_content,
            content_type="text/csv"
        )
    
    def test_fluxo_upload_e_chat_completo(self):
        """Testa o fluxo completo: upload -> chat -> análise"""
        
        # 1. Acessar página de upload
        response = self.client.get(reverse('upload'))
        assert response.status_code == 200
        
        # 2. Fazer upload do arquivo
        response = self.client.post(reverse('upload'), {
            'titulo': 'Dados Financeiros Teste',
            'arquivo': self.arquivo_csv
        })
        assert response.status_code == 302  # Redirect para chat
        
        # 3. Verificar se arquivo foi salvo
        assert UploadArquivo.objects.count() == 1
        upload = UploadArquivo.objects.first()
        assert upload.titulo == 'Dados Financeiros Teste'
        
        # 4. Acessar página de chat
        response = self.client.get(reverse('chat'))
        assert response.status_code == 200
        assert 'arquivos' in response.context
    
    def test_fluxo_analise_csv(self):
        """Testa fluxo de análise de CSV"""
        
        # 1. Criar arquivo no sistema
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("data,valor\n2024-01-01,100.50\n2024-01-02,-50.25")
            temp_path = f.name
        
        try:
            # 2. Fazer upload
            with open(temp_path, 'rb') as f:
                arquivo = SimpleUploadedFile("teste.csv", f.read(), content_type="text/csv")
            
            self.client.post(reverse('upload'), {
                'titulo': 'Teste Análise',
                'arquivo': arquivo
            })
            
            # 3. Testar chat com pergunta de análise
            response = self.client.post(reverse('chat'), {
                'pergunta': 'análise completa',
                'arquivo': 'teste.csv'
            })
            
            assert response.status_code == 200
            
        finally:
            # Limpar arquivo temporário
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_navegacao_entre_paginas(self):
        """Testa navegação entre as páginas principais"""
        
        # 1. Página inicial (upload)
        response = self.client.get('/')
        assert response.status_code == 200
        assert b'Upload' in response.content
        
        # 2. Página de chat
        response = self.client.get('/chat/')
        assert response.status_code == 200
        
        # 3. Página de teste
        response = self.client.get('/test/')
        assert response.status_code == 200
    
    def test_tratamento_erro_arquivo_inexistente(self):
        """Testa tratamento de erro quando arquivo não existe"""
        
        response = self.client.post(reverse('chat'), {
            'pergunta': 'análise',
            'arquivo': 'arquivo_inexistente.csv'
        })
        
        assert response.status_code == 200
        # Deve retornar algum tipo de erro ou mensagem