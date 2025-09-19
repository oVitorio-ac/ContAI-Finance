import pytest
from django.test import Client, TestCase
from django.urls import resolve, reverse


@pytest.mark.integration
class TestURLs(TestCase):
    """Testes de integração para as URLs"""

    def setUp(self):
        """Setup para os testes"""
        self.client = Client()

    def test_upload_url_resolve(self):
        """Testa resolução da URL de upload"""
        url = reverse('upload')
        self.assertEqual(url, '/upload/')

        resolver = resolve('/upload/')
        self.assertEqual(resolver.view_name, 'upload')

    def test_chat_url_resolve(self):
        """Testa resolução da URL de chat"""
        url = reverse('chat')
        self.assertEqual(url, '/chat/')

        resolver = resolve('/chat/')
        self.assertEqual(resolver.view_name, 'chat')

    def test_test_url_resolve(self):
        """Testa resolução da URL de teste"""
        url = reverse('test')
        self.assertEqual(url, '/test/')

        resolver = resolve('/test/')
        self.assertEqual(resolver.view_name, 'test')

    def test_urls_acessiveis(self):
        """Testa acessibilidade das URLs"""
        urls = [
            ('upload', 200),
            ('chat', 200),
            ('test', 200),
        ]

        for url_name, expected_status in urls:
            with self.subTest(url=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, expected_status)