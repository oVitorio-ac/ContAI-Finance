"""
Configuração compartilhada para testes.
"""
import os
import sys
import pytest
import django
from django.conf import settings

# Adicionar src/ ao path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contai_finance.settings')

# Inicializar Django
django.setup()


@pytest.fixture
def client():
    """Cliente de teste Django."""
    from django.test import Client
    return Client()


@pytest.fixture
def uploaded_file():
    """Arquivo de teste para upload."""
    from django.core.files.uploadedfile import SimpleUploadedFile
    return SimpleUploadedFile(
        "teste.csv",
        b"nome,valor\nTeste,100.50",
        content_type="text/csv"
    )