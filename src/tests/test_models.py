import pytest
from django.core.files.base import ContentFile
from django.test import TestCase

from financeiro.models import UploadArquivo


@pytest.mark.unit
class TestUploadArquivoModel(TestCase):
    """Testes unitários para o modelo UploadArquivo"""

    def setUp(self):
        """Setup para os testes"""
        self.titulo = "Arquivo de Teste"
        self.arquivo_content = b"col1,col2\n1,2\n3,4"
        self.arquivo = ContentFile(self.arquivo_content, name="teste.csv")

    def test_criar_upload_arquivo(self):
        """Testa criação de um UploadArquivo"""
        upload = UploadArquivo.objects.create(
            titulo=self.titulo,
            arquivo=self.arquivo
        )

        self.assertEqual(upload.titulo, self.titulo)
        self.assertTrue(upload.arquivo.name.startswith("uploads/teste"))
        self.assertTrue(upload.arquivo.name.endswith(".csv"))
        self.assertIsNotNone(upload.data_upload)
        self.assertIsNotNone(upload.pk)

    def test_str_method(self):
        """Testa o método __str__ do modelo"""
        upload = UploadArquivo.objects.create(
            titulo=self.titulo,
            arquivo=self.arquivo
        )

        self.assertEqual(str(upload), self.titulo)

    def test_meta_verbose_names(self):
        """Testa os nomes verbose do modelo"""
        meta = UploadArquivo._meta

        self.assertEqual(meta.verbose_name, "Upload de Arquivo")
        self.assertEqual(meta.verbose_name_plural, "Uploads de Arquivos")
        self.assertEqual(meta.app_label, "financeiro")