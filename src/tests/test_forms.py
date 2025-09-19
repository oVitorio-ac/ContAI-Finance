import pytest
from django.core.files.base import ContentFile
from django.test import TestCase

from financeiro.forms import UploadArquivoForm


@pytest.mark.unit
class TestUploadArquivoForm(TestCase):
    """Testes unitários para o formulário UploadArquivoForm"""

    def setUp(self):
        """Setup para os testes"""
        self.titulo_valido = "Arquivo de Teste"
        self.arquivo_content = b"col1,col2\n1,2\n3,4"
        self.arquivo_valido = ContentFile(self.arquivo_content, name="teste.csv")

    def test_form_valido(self):
        """Testa formulário com dados válidos"""
        form_data = {'titulo': self.titulo_valido}
        form_files = {'arquivo': self.arquivo_valido}

        form = UploadArquivoForm(data=form_data, files=form_files)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['titulo'], self.titulo_valido)
        self.assertEqual(form.cleaned_data['arquivo'].name, "teste.csv")

    def test_form_sem_titulo(self):
        """Testa formulário sem título"""
        form_data = {}
        form_files = {'arquivo': self.arquivo_valido}

        form = UploadArquivoForm(data=form_data, files=form_files)

        self.assertFalse(form.is_valid())
        self.assertIn('titulo', form.errors)

    def test_form_sem_arquivo(self):
        """Testa formulário sem arquivo"""
        form_data = {'titulo': self.titulo_valido}
        form_files = {}

        form = UploadArquivoForm(data=form_data, files=form_files)

        self.assertFalse(form.is_valid())
        self.assertIn('arquivo', form.errors)

    def test_form_campos_obrigatorios(self):
        """Testa que os campos são obrigatórios"""
        form = UploadArquivoForm(data={}, files={})

        self.assertFalse(form.is_valid())
        self.assertIn('titulo', form.errors)
        self.assertIn('arquivo', form.errors)