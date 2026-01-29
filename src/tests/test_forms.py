import pytest
from django.core.files.base import ContentFile
from django.test import TestCase

from financeiro.forms import UploadArquivoForm


@pytest.mark.unit
class TestUploadArquivoForm(TestCase):
    """Unit tests for the UploadArquivoForm"""

    def setUp(self):
        """Setup for tests"""
        self.titulo_valido = "Test File"
        self.arquivo_content = b"col1,col2\n1,2\n3,4"
        self.arquivo_valido = ContentFile(self.arquivo_content, name="test.csv")

    def test_form_valido(self):
        """Tests form with valid data"""
        form_data = {'titulo': self.titulo_valido}
        form_files = {'arquivo': self.arquivo_valido}

        form = UploadArquivoForm(data=form_data, files=form_files)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['titulo'], self.titulo_valido)
        self.assertEqual(form.cleaned_data['arquivo'].name, "test.csv")

    def test_form_sem_titulo(self):
        """Tests form without title"""
        form_data = {}
        form_files = {'arquivo': self.arquivo_valido}

        form = UploadArquivoForm(data=form_data, files=form_files)

        self.assertFalse(form.is_valid())
        self.assertIn('titulo', form.errors)

    def test_form_sem_arquivo(self):
        """Tests form without file"""
        form_data = {'titulo': self.titulo_valido}
        form_files = {}

        form = UploadArquivoForm(data=form_data, files=form_files)

        self.assertFalse(form.is_valid())
        self.assertIn('arquivo', form.errors)

    def test_form_campos_obrigatorios(self):
        """Tests that fields are required"""
        form = UploadArquivoForm(data={}, files={})

        self.assertFalse(form.is_valid())
        self.assertIn('titulo', form.errors)
        self.assertIn('arquivo', form.errors)