import pytest
from django.core.files.base import ContentFile
from django.test import TestCase

from financeiro.models import UploadArquivo


@pytest.mark.unit
class TestUploadArquivoModel(TestCase):
    """Unit tests for the UploadArquivo model"""

    def setUp(self):
        """Setup for tests"""
        self.titulo = "Test File"
        self.arquivo_content = b"col1,col2\n1,2\n3,4"
        self.arquivo = ContentFile(self.arquivo_content, name="test.csv")

    def test_create_upload_arquivo(self):
        """Tests creation of an UploadArquivo"""
        upload = UploadArquivo.objects.create(
            titulo=self.titulo,
            arquivo=self.arquivo
        )

        self.assertEqual(upload.titulo, self.titulo)
        self.assertTrue(upload.arquivo.name.startswith("uploads/test"))
        self.assertTrue(upload.arquivo.name.endswith(".csv"))
        self.assertIsNotNone(upload.data_upload)
        self.assertIsNotNone(upload.pk)

    def test_str_method(self):
        """Tests the __str__ method of the model"""
        upload = UploadArquivo.objects.create(
            titulo=self.titulo,
            arquivo=self.arquivo
        )

        self.assertEqual(str(upload), self.titulo)

    def test_meta_verbose_names(self):
        """Tests the verbose names of the model"""
        meta = UploadArquivo._meta

        self.assertEqual(meta.verbose_name, "File Upload")
        self.assertEqual(meta.verbose_name_plural, "File Uploads")
        self.assertEqual(meta.app_label, "financeiro")