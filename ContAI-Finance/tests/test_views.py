import pytest
import json
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from financeiro.models import UploadArquivo


@pytest.mark.integration
class TestViews(TestCase):
    """Testes de integração para as views"""
    
    def setUp(self):
        """Setup para cada teste"""
        self.client = Client()
        self.csv_content = b"nome,valor\nTeste,100.50\nOutro,200.75"
        self.arquivo_teste = SimpleUploadedFile(
            "teste.csv", 
            self.csv_content, 
            content_type="text/csv"
        )
    
    def test_upload_view_get(self):
        """Testa GET na view de upload"""
        response = self.client.get(reverse('upload'))
        
        assert response.status_code == 200
        assert 'form' in response.context
        assert b'Upload' in response.content
    
    def test_upload_view_post_valido(self):
        """Testa POST válido na view de upload"""
        response = self.client.post(reverse('upload'), {
            'titulo': 'Arquivo Teste',
            'arquivo': self.arquivo_teste
        })
        
        assert response.status_code == 302  # Redirect
        assert UploadArquivo.objects.count() == 1
        
        upload = UploadArquivo.objects.first()
        assert upload.titulo == 'Arquivo Teste'
    
    def test_upload_view_post_invalido(self):
        """Testa POST inválido na view de upload"""
        response = self.client.post(reverse('upload'), {
            'titulo': ''  # Título vazio
        })
        
        assert response.status_code == 200  # Não redireciona
        assert UploadArquivo.objects.count() == 0
    
    def test_chat_view_get(self):
        """Testa GET na view de chat"""
        response = self.client.get(reverse('chat'))
        
        assert response.status_code == 200
        assert 'arquivos' in response.context
    
    def test_chat_view_post_sem_arquivo(self):
        """Testa POST no chat sem arquivo selecionado"""
        response = self.client.post(reverse('chat'), {
            'pergunta': 'Qual o total?',
            'arquivo': ''
        })
        
        assert response.status_code == 200
        data = json.loads(response.content)
        assert 'selecione um arquivo' in data['resposta'].lower()
    
    def test_test_view_get(self):
        """Testa view de teste com GET"""
        response = self.client.get('/test/')
        
        assert response.status_code == 200
        data = json.loads(response.content)
        assert data['status'] == 'GET funcionando'
    
    def test_test_view_post(self):
        """Testa view de teste com POST"""
        response = self.client.post('/test/', {'teste': 'valor'})
        
        assert response.status_code == 200
        data = json.loads(response.content)
        assert data['status'] == 'POST funcionando'