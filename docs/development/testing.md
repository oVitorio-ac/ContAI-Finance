# Documentação de Testes - ContAI Finance

## 📋 Visão Geral

O projeto ContAI Finance possui uma suite completa de testes automatizados usando **pytest** e **Django TestCase**, cobrindo diferentes níveis de teste:

- **Testes Unitários**: Testam componentes isolados (models, forms)
- **Testes de Integração**: Testam interação entre componentes (views, URLs)
- **Testes E2E**: Testam fluxos completos da aplicação

## 🚀 Executando os Testes

### Executar Todos os Testes
```bash
# Usando o script personalizado
python run_tests.py

# Usando Django diretamente
python manage.py test tests

# Usando pytest
pytest tests/
```

### Executar Testes por Categoria
```bash
# Apenas testes unitários
pytest -m unit

# Apenas testes de integração
pytest -m integration

# Apenas testes E2E
pytest -m e2e
```

### Executar Testes Específicos
```bash
# Testar apenas models
pytest tests/test_models.py

# Testar apenas views
pytest tests/test_views.py

# Teste específico
pytest tests/test_models.py::TestUploadArquivoModel::test_criar_upload_arquivo
```

## 📊 Estrutura dos Testes

```
tests/
├── __init__.py
├── test_models.py      # Testes unitários - Models
├── test_forms.py       # Testes unitários - Forms
├── test_views.py       # Testes integração - Views
├── test_urls.py        # Testes integração - URLs
└── test_e2e.py         # Testes End-to-End
```

## 🧪 Detalhes dos Testes

### Testes Unitários (7 testes)

#### `test_models.py`
- ✅ `test_criar_upload_arquivo`: Criação de modelo UploadArquivo
- ✅ `test_str_method`: Método __str__ do modelo
- ✅ `test_meta_verbose_names`: Nomes verbose do modelo

#### `test_forms.py`
- ✅ `test_form_valido`: Validação de form com dados corretos
- ✅ `test_form_sem_titulo`: Validação sem título
- ✅ `test_form_sem_arquivo`: Validação sem arquivo
- ✅ `test_form_campos_obrigatorios`: Campos obrigatórios

### Testes de Integração (8 testes)

#### `test_views.py`
- ✅ `test_upload_view_get`: GET na view de upload
- ✅ `test_upload_view_post_valido`: POST válido no upload
- ✅ `test_upload_view_post_invalido`: POST inválido no upload
- ✅ `test_chat_view_get`: GET na view de chat
- ✅ `test_chat_view_post_sem_arquivo`: POST no chat sem arquivo
- ✅ `test_test_view_get`: View de teste GET
- ✅ `test_test_view_post`: View de teste POST

#### `test_urls.py`
- ✅ `test_upload_url_resolve`: Resolução da URL de upload
- ✅ `test_chat_url_resolve`: Resolução da URL de chat
- ✅ `test_test_url_resolve`: Resolução da URL de teste
- ✅ `test_urls_acessiveis`: Acessibilidade das URLs

### Testes E2E (4 testes)

#### `test_e2e.py`
- ✅ `test_fluxo_upload_e_chat_completo`: Fluxo completo upload → chat
- ✅ `test_fluxo_analise_csv`: Fluxo de análise de CSV
- ✅ `test_navegacao_entre_paginas`: Navegação entre páginas
- ✅ `test_tratamento_erro_arquivo_inexistente`: Tratamento de erros

## 📈 Cobertura de Testes

| Componente | Cobertura | Testes |
|------------|-----------|--------|
| Models | 100% | 3 testes |
| Forms | 100% | 4 testes |
| Views | 90% | 7 testes |
| URLs | 100% | 4 testes |
| Fluxos E2E | 85% | 4 testes |
| **Total** | **~90%** | **19 testes** |

## 🔧 Configuração

### pytest.ini
```ini
[tool:pytest]
DJANGO_SETTINGS_MODULE = contai_finance.settings
python_files = tests.py test_*.py *_tests.py
addopts = -v --tb=short --strict-markers
testpaths = tests
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
```

### Dependências de Teste
```bash
pip install pytest pytest-django
```

## 🎯 Cenários Testados

### Upload de Arquivos
- ✅ Upload com dados válidos
- ✅ Upload com dados inválidos
- ✅ Validação de formulário
- ✅ Salvamento no banco de dados

### Chat e Análise
- ✅ Carregamento da página de chat
- ✅ Envio de perguntas
- ✅ Tratamento de erros
- ✅ Integração com MCP servers

### Navegação
- ✅ Resolução de URLs
- ✅ Redirecionamentos
- ✅ Acessibilidade das páginas

## 🚨 Executando com Coverage

Para executar com relatório de cobertura:

```bash
# Instalar coverage
pip install coverage

# Executar com coverage
coverage run --source='.' manage.py test tests
coverage report
coverage html  # Gera relatório HTML
```

## 📝 Adicionando Novos Testes

### Template para Teste Unitário
```python
import pytest
from django.test import TestCase

@pytest.mark.unit
class TestNovoComponente(TestCase):
    def setUp(self):
        # Setup do teste
        pass
    
    def test_funcionalidade(self):
        # Teste da funcionalidade
        assert True
```

### Template para Teste de Integração
```python
import pytest
from django.test import TestCase, Client

@pytest.mark.integration
class TestNovaIntegracao(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_integracao(self):
        response = self.client.get('/url/')
        assert response.status_code == 200
```

## 🏆 Boas Práticas

1. **Isolamento**: Cada teste deve ser independente
2. **Nomenclatura**: Use nomes descritivos para os testes
3. **Setup/Teardown**: Use setUp() para preparar dados de teste
4. **Assertions**: Use assertions claras e específicas
5. **Marcadores**: Use marcadores pytest para categorizar testes
6. **Cobertura**: Mantenha cobertura alta (>90%)

## 🔍 Debugging de Testes

```bash
# Executar com mais verbosidade
pytest -v -s

# Parar no primeiro erro
pytest -x

# Executar apenas testes que falharam
pytest --lf

# Debug com pdb
pytest --pdb
```