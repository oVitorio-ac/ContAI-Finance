import pytest
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from src.financeiro.forms import UploadArquivoForm


@pytest.mark.unit
class TestUploadArquivoForm(TestCase):
    """Testes unitários para o form UploadArquivoForm"""
    
    def setUp(self):
        """Setup para cada teste"""
        self.csv_content = b"nome,valor\nTeste,100.50"
        self.arquivo_valido = SimpleUploadedFile(
            "teste.csv", 
            self.csv_content, 
            content_type="text/csv"
        )
    
    def test_form_valido(self):
        """Testa form com dados válidos"""
        form_data = {'titulo': 'Arquivo Teste'}
        form_files = {'arquivo': self.arquivo_valido}
        
        form = UploadArquivoForm(data=form_data, files=form_files)
        
        assert form.is_valid()
    
    def test_form_sem_titulo(self):
        """Testa form sem título"""
        form_data = {}
        form_files = {'arquivo': self.arquivo_valido}
        
        form = UploadArquivoForm(data=form_data, files=form_files)
        
        assert not form.is_valid()
        assert 'titulo' in form.errors
    
    def test_form_sem_arquivo(self):
        """Testa form sem arquivo"""
        form_data = {'titulo': 'Teste'}
        
        form = UploadArquivoForm(data=form_data)
        
        assert not form.is_valid()
        assert 'arquivo' in form.errors
    
    def test_form_campos_obrigatorios(self):
        """Testa se os campos obrigatórios estão corretos"""
        form = UploadArquivoForm()
        
        assert 'titulo' in form.fields
        assert 'arquivo' in form.fields
        assert len(form.fields) == 2