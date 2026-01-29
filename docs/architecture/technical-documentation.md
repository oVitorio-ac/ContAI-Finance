# Technical Documentation - ContAI Finance

## 📋 Project Overview

ContAI Finance is a Django web application developed for accountants to upload CSV files and interact with an AI assistant for financial data analysis.

## 🏗️ System Architecture

### Main Components

1. **Frontend**: Responsive web interface using Bootstrap 5.
2. **Backend**: Django 5.2.6 with Python 3.12+.
3. **Database**: SQLite for development.
4. **MCP Servers**: Specialized CSV analysis and Bedrock integration servers.
5. **Infrastructure**: Docker + Terraform for AWS deployment.

### Data Flow

```text
User → Frontend → Django Views → MCP Servers → AWS Bedrock
                         ↓
                   SQLite Database
                         ↓
                   Media Storage
```

## 🔧 Technologies Used

| Category | Technology | Version | Purpose |
| :--- | :--- | :--- | :--- |
| **Backend** | Django | 5.2.6 | Web Framework |
| **Frontend** | Bootstrap | 5.x | Responsive UI |
| **Database** | SQLite | 3.x | Database |
| **Cloud** | AWS Bedrock | - | AI for Analysis |
| **Cloud** | AWS S3 | - | Storage |
| **Testing** | pytest | 7.4.3 | Automated Testing |
| **Package Management** | Poetry | - | Dependency Management |
| **Linting** | Ruff | - | Fast Linting and Formatting |
| **Formatting** | Black | 23.7.0 | Code Formatting |
| **Import Sorting** | isort | 5.12.0 | Import Organization |
| **IaC** | Terraform | 1.x | Infrastructure as Code |
| **Container** | Docker | - | Containerization |

## 📁 Project Structure

```text
ContAI-Finance/
├── src/                          # 📁 Source Code
│   ├── contai_finance/          # 🏗️ Django Configuration
│   │   ├── settings.py         # Main Settings
│   │   ├── urls.py            # Main URLs
│   │   └── wsgi.py            # WSGI Config
│   ├── financeiro/             # 📦 Main Application Module
│   │   ├── models.py          # Data Models
│   │   ├── views.py           # Business Logic
│   │   ├── forms.py           # Forms
│   │   └── urls.py            # Application URLs
│   ├── mcp_server/            # 🔧 Utilities/Services
│   │   ├── csv_analyzer.py    # CSV Analysis
│   │   └── bedrock_integration.py # Bedrock Integration
│   ├── templates/              # 📄 HTML Templates
│   │   ├── base.html          # Base Template
│   │   ├── upload.html        # Upload Page
│   │   └── chat.html          # Chat Page
│   ├── static/                 # 🎨 Static Assets
│   └── manage.py               # 🎯 Entry Point
├── tests/                        # 🧪 Organized Tests
│   ├── conftest.py             # Shared Configuration
│   ├── test_models.py          # Model Tests
│   ├── test_forms.py           # Form Tests
│   ├── test_views.py           # View Tests
│   └── test_urls.py            # URL Tests
├── infrastructure/               # ☁️ Infrastructure as Code
│   ├── terraform/              # 🏗️ AWS IaC
│   │   ├── main.tf            # Terraform Config
│   │   ├── variables.tf       # Variables
│   │   └── outputs.tf         # Outputs
│   ├── docker/                 # 🐳 Containerization
│   │   └── Dockerfile         # Docker Image
│   └── scripts/                # 📜 Deployment Scripts
│       ├── deploy.sh          # Deployment Script
│       └── lambda_function.py # Lambda Function
├── docs/                         # 📚 Comprehensive Documentation
├── .env.example                  # 🔐 Environment Variables Example
├── manage.py                     # 🎯 Wrapper for src/manage.py
├── pytest.ini                    # ⚙️ Test Configuration
├── .pre-commit-config.yaml       # 🔧 Pre-commit Hooks
└── README.md                     # 📖 Main Documentation
```

## 🗄️ Data Models

### UploadArquivo (Uploaded File)

```python
class UploadArquivo(models.Model):
    titulo = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='uploads/')
    data_upload = models.DateTimeField(auto_now_add=True)
```

**Fields:**

- `titulo`: Descriptive name of the file.
- `arquivo`: The uploaded CSV file.
- `data_upload`: Timestamp of the upload.

## 🌐 APIs and Endpoints

### Main URLs

| URL | Method | View | Description |
| :--- | :--- | :--- | :--- |
| `/` | GET/POST | `upload_view` | File Upload |
| `/chat/` | GET/POST | `chat_view` | Chat Interface |
| `/test/` | GET/POST | `test_view` | Test Endpoint |

### Chat Response Format

```json
{
  "response": "Analysis of financial.csv:\n📊 Total: $ 1,500.00"
}
```

## 🔍 MCP Servers

The project uses the **Model Context Protocol (MCP)** to provide the AI with specialized tools for data analysis.

### CSV Analyzer

- **File**: `src/mcp_server/csv_analyzer.py`
- **Function**: Performs local analysis of CSV files using `pandas`.
- **Capabilities**:
  - **File Listing**: Scan the `media/uploads` directory for available CSVs.
  - **Structural Analysis**: Detect columns, data types, and missing values.
  - **Financial Heuristics**: Automatically identify "value" and "date" columns based on common patterns (e.g., "valor", "amount", "date").
  - **Query Engine**: Execute pre-defined mathematical operations like `total`, `average`, `max`, and `min` on the data.

### Bedrock Integration

- **File**: `src/mcp_server/bedrock_integration.py`
- **Function**: Interfaces with **Anthropic Claude 3 Haiku** via AWS Bedrock.
- **Capabilities**:
  - **Intelligent Insight Generation**: Summarize financial trends and provide qualitative analysis.
  - **Advanced Query Support**: Handle natural language questions that require cross-referencing or complex reasoning.
  - **Period Comparison**: Automatically group data by time periods and calculate growth/decline rates.
  - **Graceful Fallback**: Includes a local analysis mode for when AWS credentials are not configured.

## 🧪 Automated Testing

### Test Structure

- **19 tests** implemented.
- **Coverage**: ~90% of code.
- **Types**: Unit, Integration, E2E.

### Running Tests

```bash
# Run all tests
python run_tests.py

# Run by category
pytest -m unit          # Unit tests
pytest -m integration   # Integration tests
pytest -m e2e           # End-to-End tests
```

## 🚀 Deployment and Infrastructure

### Local Development

1. **Clone repository**
   ```bash
   git clone https://github.com/oVitorio-ac/ContAI-Finance.git
   cd ContAI-Finance
   ```
2. **Setup environment using Poetry**
   ```bash
   poetry install
   ```
3. **Configure environment variables (optional)**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```
4. **Run migrations**
   ```bash
   poetry run python manage.py migrate
   ```
5. **Start server**
   ```bash
   poetry run python manage.py runserver
   ```

### Development Configuration

The project follows high standards for code quality and maintainability:

1. **Dependency Management**: Powered by **Poetry**, ensuring reproducible builds and isolated environments.
2. **Linting & Formatting**:
   - **Ruff**: used as a hyper-fast linter and formatter.
   - **Black**: provides consistent, unopinionated code styling.
   - **isort**: handles import sorting automatically.
3. **Pre-commit Hooks**: Enforce quality checks before every commit to prevent regression.
4. **Environment Isolation**: Uses `.env` files for sensitive configuration, following the "Twelve-Factor App" methodology.

```bash
# Install pre-commit hooks
poetry run pre-commit install

# Run linting and formatting
poetry run ruff check src/
poetry run ruff format src/
poetry run black src/
poetry run isort src/

# Run tests with coverage
poetry run pytest --cov=src --cov-report=html
```

### AWS Deployment (Planned)

- **ECS Fargate**: Application containers.
- **S3**: File storage.
- **Lambda**: Serverless processing.
- **ALB**: Application Load Balancer.
- **Terraform**: Infrastructure as Code.

## 🔒 Security

### Security Features

- CSRF protection enabled.
- File upload validation.
- SQL injection protection (Django ORM).
- XSS protection (Django templates).

### Environment Variables

```bash
# AWS (Production)
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<secret>
AWS_S3_BUCKET_NAME=<bucket>
AWS_REGION=us-east-1

# Django
DEBUG=False
SECRET_KEY=<secret>
ALLOWED_HOSTS=<hosts>
```

## 📊 Monitoring and Logs

### Logging

```python
# Configuration in settings.py
LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'contai_finance.log',
        },
    },
    'loggers': {
        'financeiro': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}
```

## 🔧 Development Settings

### Main settings.py

```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

## 🐛 Troubleshooting

### Common Issues

1. **ALLOWED_HOSTS Error**
   ```python
   # settings.py
   ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-domain.com']
   ```

2. **Migration Errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Static Files Error**
   ```bash
   python manage.py collectstatic
   ```

## 📈 Performance

### Implemented Optimizations

- Lazy loading for MCP servers.
- CSV analysis caching.
- Response compression.
- Django query optimization.

### Performance Metrics

- Upload time: < 2s
- CSV analysis: < 5s
- Chat response: < 3s

## 🔄 CI/CD (Planned)

### GitHub Actions Pipeline

```yaml
# .github/workflows/ci.yml
name: CI/CD
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: python run_tests.py
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to AWS
        run: terraform apply
```

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [AWS Bedrock Docs](https://docs.aws.amazon.com/bedrock/)
- [Bootstrap Docs](https://getbootstrap.com/docs/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/)

## 🤝 Contributing

1. Fork the project.
2. Create your feature branch.
3. Implement tests.
4. Run the test suite.
5. Commit your changes.
6. Open a Pull Request.