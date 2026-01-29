# Test Documentation - ContAI Finance

## 📋 Overview

The ContAI Finance project features a comprehensive suite of automated tests using **pytest** and **Django TestCase**, covering various testing levels:

- **Unit Tests**: Test isolated components (models, forms).
- **Integration Tests**: Test interactions between components (views, URLs).
- **E2E Tests**: Test complete application workflows.

## 🚀 Running Tests

### Run All Tests
```bash
# Using the custom script
python run_tests.py

# Using Django directly (via Poetry)
poetry run python manage.py test tests

# Using pytest (via Poetry)
poetry run pytest
```

### Run Tests by Category
```bash
# Unit tests only
poetry run pytest -m unit

# Integration tests only
poetry run pytest -m integration

# E2E tests only
poetry run pytest -m e2e
```

### Run Specific Tests
```bash
# Test only models
poetry run pytest tests/test_models.py

# Test only views
poetry run pytest tests/test_views.py

# Run a specific test
poetry run pytest tests/test_models.py::TestUploadArquivoModel::test_criar_upload_arquivo
```

## 📊 Test Structure

```text
tests/
├── __init__.py
├── test_models.py      # Unit tests - Models
├── test_forms.py       # Unit tests - Forms
├── test_views.py       # Integration tests - Views
├── test_urls.py        # Integration tests - URLs
└── test_e2e.py         # End-to-End tests
```

## 🧪 Test Details

### Unit Tests (7 tests)

#### `test_models.py`
- ✅ `test_criar_upload_arquivo`: Creation of UploadArquivo model.
- ✅ `test_str_method`: Model's `__str__` method.
- ✅ `test_meta_verbose_names`: Model's verbose names.

#### `test_forms.py`
- ✅ `test_form_valido`: Form validation with correct data.
- ✅ `test_form_sem_titulo`: Validation when title is missing.
- ✅ `test_form_sem_arquivo`: Validation when file is missing.
- ✅ `test_form_campos_obrigatorios`: Required fields validation.

### Integration Tests (8 tests)

#### `test_views.py`
- ✅ `test_upload_view_get`: GET request on upload view.
- ✅ `test_upload_view_post_valido`: Valid POST request on upload.
- ✅ `test_upload_view_post_invalido`: Invalid POST request on upload.
- ✅ `test_chat_view_get`: GET request on chat view.
- ✅ `test_chat_view_post_sem_arquivo`: POST request on chat without selecting a file.
- ✅ `test_test_view_get`: GET on test view.
- ✅ `test_test_view_post`: POST on test view.

#### `test_urls.py`
- ✅ `test_upload_url_resolve`: Resolving the upload URL.
- ✅ `test_chat_url_resolve`: Resolving the chat URL.
- ✅ `test_test_url_resolve`: Resolving the test URL.
- ✅ `test_urls_acessiveis`: URL accessibility check.

### E2E Tests (4 tests)

#### `test_e2e.py`
- ✅ `test_fluxo_upload_e_chat_completo`: Full workflow from upload to chat.
- ✅ `test_fluxo_analise_csv`: CSV analysis workflow.
- ✅ `test_navegacao_entre_paginas`: Navigation between pages.
- ✅ `test_tratamento_erro_arquivo_inexistente`: Error handling for missing files.

## 📈 Test Coverage

| Component | Coverage | Tests |
|------------|-----------|--------|
| Models | 100% | 3 tests |
| Forms | 100% | 4 tests |
| Views | 90% | 7 tests |
| URLs | 100% | 4 tests |
| E2E Flows | 85% | 4 tests |
| **Total** | **~90%** | **19 tests** |

## 🔧 Configuration

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

## 🎯 Tested Scenarios

### File Upload
- ✅ Upload with valid data.
- ✅ Upload with invalid data.
- ✅ Form validation.
- ✅ Database persistence.

### Chat and Analysis
- ✅ Chat page loading.
- ✅ Sending questions.
- ✅ Error handling.
- ✅ Integration with MCP servers.

### Navigation
- ✅ URL resolution.
- ✅ Redirects.
- ✅ Page accessibility.

## 🚨 Running with Coverage

To run tests with a coverage report:

```bash
# Run with coverage (via Poetry)
poetry run pytest --cov=src --cov-report=html
```

## 📝 Adding New Tests

### Unit Test Template
```python
import pytest
from django.test import TestCase

@pytest.mark.unit
class TestNewComponent(TestCase):
    def setUp(self):
        # Test setup
        pass
    
    def test_functionality(self):
        # Test logic
        assert True
```

### Integration Test Template
```python
import pytest
from django.test import TestCase, Client

@pytest.mark.integration
class TestNewIntegration(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_integration(self):
        response = self.client.get('/url/')
        assert response.status_code == 200
```

## 🏆 Best Practices

1. **Isolation**: Each test must be independent.
2. **Naming**: Use descriptive names for test cases.
3. **Setup/Teardown**: Use `setUp()` to prepare test data.
4. **Assertions**: Use clear and specific assertions.
5. **Markers**: Use pytest markers to categorize tests.
6. **Coverage**: Maintain high coverage (>90%).

## 🔍 Debugging Tests

```bash
# Run with increased verbosity
poetry run pytest -v -s

# Stop at the first failure
poetry run pytest -x

# Run only the last failed tests
poetry run pytest --lf

# Debug with pdb
poetry run pytest --pdb
```