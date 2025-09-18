import pytest
from django.test import TestCase
from django.urls import reverse, resolve
from financeiro.views import upload_view, chat_view, test_view


@pytest.mark.integration
class TestUrls(TestCase):
    """Testes de integração para URLs"""
    
    def test_upload_url_resolve(self):
        """Testa se a URL de upload resolve corretamente"""
        url = reverse('upload')
        assert url == '/'
        
        resolver = resolve(url)
        assert resolver.func == upload_view
    
    def test_chat_url_resolve(self):
        """Testa se a URL de chat resolve corretamente"""
        url = reverse('chat')
        assert url == '/chat/'
        
        resolver = resolve(url)
        assert resolver.func == chat_view
    
    def test_test_url_resolve(self):
        """Testa se a URL de teste resolve corretamente"""
        resolver = resolve('/test/')
        assert resolver.func == test_view
    
    def test_urls_acessiveis(self):
        """Testa se as URLs principais são acessíveis"""
        urls_para_testar = [
            ('upload', '/'),
            ('chat', '/chat/'),
        ]
        
        for name, expected_url in urls_para_testar:
            with self.subTest(name=name):
                url = reverse(name)
                assert url == expected_url