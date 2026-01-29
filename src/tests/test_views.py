import pytest
from unittest.mock import patch
from django.core.files.base import ContentFile
from django.test import Client, TestCase
from django.urls import reverse

from financeiro.models import UploadArquivo


@pytest.mark.integration
class TestViews(TestCase):
    """Integration tests for views"""

    def setUp(self):
        """Setup for tests"""
        self.client = Client()
        self.arquivo_content = b"col1,col2\n1,2\n3,4"
        self.arquivo = ContentFile(self.arquivo_content, name="test.csv")

    def test_upload_view_get(self):
        """Tests GET on upload view"""
        response = self.client.get(reverse('upload'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')
        self.assertIn('form', response.context)

    def test_upload_view_post_valid(self):
        """Tests valid POST on upload"""
        form_data = {'titulo': 'Test File'}
        form_files = {'arquivo': self.arquivo}

        response = self.client.post(reverse('upload'), data=form_data, files=form_files)

        # Check if saved in DB
        upload = UploadArquivo.objects.first()
        if upload:
            # Should redirect to chat if saved
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, reverse('chat'))
            self.assertEqual(upload.titulo, 'Test File')
        else:
            # Check if page rendered correctly
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'upload.html')

    def test_upload_view_post_invalid(self):
        """Tests invalid POST on upload"""
        # Missing title
        form_data = {}
        form_files = {'arquivo': self.arquivo}

        response = self.client.post(reverse('upload'), data=form_data, files=form_files)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())

    def test_chat_view_get(self):
        """Tests GET on chat view"""
        with patch("financeiro.views.CSVAnalyzer") as mock_analyzer:
            instance = mock_analyzer.return_value
            instance.list_csv_files.return_value = [{"filename": "test.csv", "rows": 10}]
            
            response = self.client.get(reverse('chat'))

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'chat.html')
            self.assertIn('arquivos', response.context)

    def test_chat_view_post_no_file(self):
        """Tests POST on chat without file selected"""
        data = {'question': 'What is the total?'}

        response = self.client.post(reverse('chat'), data=data)

        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn('response', json_response)
        self.assertIn('Please select a CSV file first', json_response['response'])

    def test_test_view_get(self):
        """Tests GET on test view"""
        response = self.client.get(reverse('test'))

        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['status'], 'GET working')
        self.assertEqual(json_response['method'], 'GET')

    def test_test_view_post(self):
        """Tests POST on test view"""
        data = {'test': 'value'}

        response = self.client.post(reverse('test'), data=data)

        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['status'], 'POST working')
        self.assertIn('test', json_response['data'])