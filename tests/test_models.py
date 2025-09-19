import pytest
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from src.financeiro.models import UploadArquivo


@pytest.mark.unit
class TestUploadArquivoModel(TestCase):
    """Testes unitários para o model UploadArquivo"""
    
    def setUp(self):
        """Setup para cada teste"""
        self.csv_content = b"nome,valor\nTeste,100.50"
        self.arquivo_teste = SimpleUploadedFile(
            "teste.csv", 
            self.csv_content, 
            content_type="text/csv"
        )
    
    def test_criar_upload_arquivo(self):
        """Testa criação de um upload de arquivo"""
        upload = UploadArquivo.objects.create(
            titulo="Arquivo de Teste",
            arquivo=self.arquivo_teste
        )
        
        assert upload.titulo == "Arquivo de Teste"
        assert upload.arquivo.name.endswith("teste.csv")
        assert upload.data_upload is not None
    
    def test_str_method(self):
        """Testa o método __str__ do model"""
        upload = UploadArquivo.objects.create(
            titulo="Teste String",
            arquivo=self.arquivo_teste
        )
        
        assert str(upload) == "Teste String"
    
    def test_meta_verbose_names(self):
        """Testa os nomes verbose do model"""
        meta = UploadArquivo._meta
        assert meta.verbose_name == "Upload de Arquivo"
        assert meta.verbose_name_plural == "Uploads de Arquivos"