import pytest
from django.test import Client, TestCase
from django.urls import resolve, reverse


@pytest.mark.integration
class TestURLs(TestCase):
    """Integration tests for URLs"""

    def setUp(self):
        """Setup for tests"""
        self.client = Client()

    def test_upload_url_resolve(self):
        """Tests resolution of the upload URL"""
        url = reverse('upload')
        self.assertEqual(url, '/upload/')

        resolver = resolve('/upload/')
        self.assertEqual(resolver.view_name, 'upload')

    def test_chat_url_resolve(self):
        """Tests resolution of the chat URL"""
        url = reverse('chat')
        self.assertEqual(url, '/chat/')

        resolver = resolve('/chat/')
        self.assertEqual(resolver.view_name, 'chat')

    def test_test_url_resolve(self):
        """Tests resolution of the test URL"""
        url = reverse('test')
        self.assertEqual(url, '/test/')

        resolver = resolve('/test/')
        self.assertEqual(resolver.view_name, 'test')

    def test_urls_acessiveis(self):
        """Tests accessibility of URLs"""
        urls = [
            ('upload', 200),
            ('chat', 200),
            ('test', 200),
        ]

        for url_name, expected_status in urls:
            with self.subTest(url=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, expected_status)