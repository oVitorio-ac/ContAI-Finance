# Documentação Técnica - ContAI Finance

## 📋 Visão Geral do Projeto

ContAI Finance é uma aplicação web Django desenvolvida para contadores fazerem upload de arquivos CSV e interagirem com um assistente de IA para análise de dados financeiros.

## 🏗️ Arquitetura do Sistema

### Componentes Principais

1. **Frontend**: Interface web responsiva com Bootstrap 5
2. **Backend**: Django 5.2.6 com Python 3.8+
3. **Banco de Dados**: SQLite para desenvolvimento
4. **MCP Servers**: Servidores de análise CSV e integração Bedrock
5. **Infraestrutura**: Docker + Terraform para deploy AWS

### Fluxo de Dados

```
Usuário → Frontend → Django Views → MCP Servers → AWS Bedrock
                         ↓
                   SQLite Database
                         ↓
                   Media Storage
```

## 🔧 Tecnologias Utilizadas

| Categoria | Tecnologia | Versão | Propósito |
|-----------|------------|--------|-----------|
| **Backend** | Django | 5.2.6 | Framework web |
| **Frontend** | Bootstrap | 5.x | UI responsiva |
| **Database** | SQLite | 3.x | Banco de dados |
| **Cloud** | AWS Bedrock | - | IA para análise |
| **Cloud** | AWS S3 | - | Armazenamento |
| **Testing** | pytest | 7.4.3 | Testes automatizados |
| **IaC** | Terraform | 1.x | Infraestrutura |
| **Container** | Docker | - | Containerização |

## 📁 Estrutura do Projeto

```
ContAI-Finance/
├── contai_finance/          # Configurações Django
│   ├── settings.py         # Configurações principais
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # WSGI config
├── financeiro/             # App principal
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Lógica de negócio
│   ├── forms.py           # Formulários
│   └── urls.py            # URLs do app
├── templates/              # Templates HTML
│   ├── base.html          # Template base
│   ├── upload.html        # Página de upload
│   └── chat.html          # Página de chat
├── static/                 # Arquivos estáticos
├── media/                  # Uploads de usuário
├── mcp_server/            # Servidores MCP
│   ├── csv_analyzer.py    # Análise de CSV
│   └── bedrock_integration.py # Integração Bedrock
├── infrastructure/         # Infraestrutura como código
│   ├── main.tf           # Terraform principal
│   └── deploy.sh         # Script de deploy
├── tests/                 # Testes automatizados
├── docs/                  # Documentação
└── requirements.txt       # Dependências Python
```

## 🗄️ Modelos de Dados

### UploadArquivo
```python
class UploadArquivo(models.Model):
    titulo = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='uploads/')
    data_upload = models.DateTimeField(auto_now_add=True)
```

**Campos:**
- `titulo`: Nome descritivo do arquivo
- `arquivo`: Arquivo CSV enviado
- `data_upload`: Timestamp do upload

## 🌐 APIs e Endpoints

### URLs Principais

| URL | Método | View | Descrição |
|-----|--------|------|-----------|
| `/` | GET/POST | `upload_view` | Upload de arquivos |
| `/chat/` | GET/POST | `chat_view` | Interface de chat |
| `/test/` | GET/POST | `test_view` | Endpoint de teste |

### Formato de Resposta do Chat

```json
{
  "resposta": "Análise do arquivo financeiro.csv:\n📊 Total: R$ 1.500,00"
}
```

## 🔍 MCP Servers

### CSV Analyzer
- **Arquivo**: `mcp_server/csv_analyzer.py`
- **Função**: Análise local de arquivos CSV
- **Métodos**:
  - `analyze_csv()`: Análise completa
  - `query_data()`: Consultas específicas
  - `list_csv_files()`: Lista arquivos disponíveis

### Bedrock Integration
- **Arquivo**: `mcp_server/bedrock_integration.py`
- **Função**: Integração com AWS Bedrock para IA
- **Métodos**:
  - `generate_financial_insights()`: Insights automáticos
  - `analyze_with_bedrock()`: Análise avançada

## 🧪 Testes Automatizados

### Estrutura de Testes
- **19 testes** implementados
- **Cobertura**: ~90% do código
- **Tipos**: Unitários, Integração, E2E

### Executar Testes
```bash
# Todos os testes
python run_tests.py

# Por categoria
pytest -m unit      # Unitários
pytest -m integration  # Integração
pytest -m e2e       # End-to-End
```

## 🚀 Deploy e Infraestrutura

### Desenvolvimento Local
```bash
# 1. Clonar repositório
git clone https://github.com/seu-usuario/ContAI-Finance.git

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar migrações
python manage.py migrate

# 4. Iniciar servidor
python manage.py runserver
```

### Deploy AWS (Planejado)
- **ECS Fargate**: Containers da aplicação
- **S3**: Armazenamento de arquivos
- **Lambda**: Processamento serverless
- **ALB**: Load balancer
- **Terraform**: Infraestrutura como código

## 🔒 Segurança

### Configurações de Segurança
- CSRF protection habilitado
- File upload validation
- SQL injection protection (Django ORM)
- XSS protection (Django templates)

### Variáveis de Ambiente
```bash
# AWS (para produção)
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<secret>
AWS_S3_BUCKET_NAME=<bucket>
AWS_REGION=us-east-1

# Django
DEBUG=False
SECRET_KEY=<secret>
ALLOWED_HOSTS=<hosts>
```

## 📊 Monitoramento e Logs

### Logging
```python
# Configuração em settings.py
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

## 🔧 Configurações de Desenvolvimento

### Settings.py Principais
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

### Problemas Comuns

1. **Erro de ALLOWED_HOSTS**
   ```python
   # settings.py
   ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'seu-dominio.com']
   ```

2. **Erro de migrações**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Erro de arquivos estáticos**
   ```bash
   python manage.py collectstatic
   ```

## 📈 Performance

### Otimizações Implementadas
- Lazy loading de MCP servers
- Caching de análises CSV
- Compressão de responses
- Otimização de queries Django

### Métricas de Performance
- Tempo de upload: < 2s
- Análise CSV: < 5s
- Resposta do chat: < 3s

## 🔄 CI/CD (Planejado)

### Pipeline GitHub Actions
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

## 📚 Recursos Adicionais

- [Documentação Django](https://docs.djangoproject.com/)
- [AWS Bedrock Docs](https://docs.aws.amazon.com/bedrock/)
- [Bootstrap Docs](https://getbootstrap.com/docs/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/)

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Implemente os testes
4. Execute a suite de testes
5. Faça commit das mudanças
6. Abra um Pull Request