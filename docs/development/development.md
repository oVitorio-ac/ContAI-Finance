# 🛠️ Guia de Desenvolvimento - ContAI Finance

Este documento contém instruções detalhadas para configurar e trabalhar no projeto usando Poetry.

## 📋 Pré-requisitos

- **Python 3.8+**
- **Poetry** (gerenciador de dependências)
- **Git**

## 🚀 Configuração Inicial

### 1. Instalar Poetry

```bash
# Instalar Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Verificar instalação
poetry --version
```

### 2. Clonar e Configurar Projeto

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/ContAI-Finance.git
cd ContAI-Finance

# Instalar dependências de desenvolvimento
poetry install --with dev

# Ativar shell do Poetry (opcional)
poetry shell
```

### 3. Configurar Ambiente

```bash
# Copiar arquivo de exemplo de variáveis de ambiente
cp .env.example .env

# Editar .env com suas configurações
nano .env
```

### 4. Configurar Pre-commit Hooks

```bash
# Instalar hooks
poetry run pre-commit install

# Executar hooks em todos os arquivos
poetry run pre-commit run --all-files
```

## 🏃‍♂️ Executando o Projeto

### Desenvolvimento Local

```bash
# Executar migrações
poetry run python manage.py migrate

# Criar superusuário (opcional)
poetry run python manage.py createsuperuser

# Iniciar servidor de desenvolvimento
poetry run python manage.py runserver
```

### Executando Testes

```bash
# Todos os testes
poetry run pytest

# Testes com cobertura
poetry run pytest --cov=src --cov-report=html

# Testes por categoria
poetry run pytest -m unit        # Testes unitários
poetry run pytest -m integration # Testes de integração
poetry run pytest -m e2e         # Testes end-to-end

# Testes específicos
poetry run pytest tests/test_models.py
poetry run pytest tests/test_views.py::TestViews::test_upload_view_get
```

## 🛠️ Ferramentas de Desenvolvimento

### Formatação e Linting

```bash
# Formatar código com Black
poetry run black src/

# Organizar imports com isort
poetry run isort src/

# Linting com Ruff
poetry run ruff check src/
poetry run ruff format src/

# Corrigir automaticamente
poetry run ruff check src/ --fix
```

### Verificação de Segurança

```bash
# Verificar vulnerabilidades
poetry run safety check

# Verificar licenças
poetry run pip-licenses
```

## 📦 Gerenciamento de Dependências

### Adicionar Dependências

```bash
# Dependência principal
poetry add requests

# Dependência de desenvolvimento
poetry add --group dev pytest-cov

# Dependência de produção
poetry add --group prod psycopg2-binary
```

### Atualizar Dependências

```bash
# Atualizar todas as dependências
poetry update

# Atualizar dependência específica
poetry update requests

# Mostrar dependências desatualizadas
poetry show --outdated
```

### Exportar Requirements (se necessário)

```bash
# Para desenvolvimento
poetry export -f requirements.txt --with dev -o requirements-dev.txt

# Para produção
poetry export -f requirements.txt --only main,prod -o requirements.txt
```

## 🐳 Docker (Opcional)

### Construir Imagem

```bash
# Construir imagem
docker build -f infrastructure/docker/Dockerfile -t contai-finance .

# Executar container
docker run -p 8000:8000 contai-finance
```

### Usando Docker Compose

```bash
# Se existir docker-compose.yml
docker-compose up -d
```

## 🚀 Deploy

### Produção

```bash
# Instalar apenas dependências de produção
poetry install --only main,prod

# Coletar arquivos estáticos
poetry run python manage.py collectstatic --noinput

# Executar migrações
poetry run python manage.py migrate

# Iniciar servidor com Gunicorn
poetry run gunicorn contai_finance.wsgi:application --bind 0.0.0.0:8000
```

### AWS (Terraform)

```bash
# Inicializar Terraform
cd infrastructure/terraform
terraform init

# Planejar mudanças
terraform plan

# Aplicar mudanças
terraform apply
```

## 🔧 Comandos Úteis

### Poetry

```bash
# Mostrar informações do projeto
poetry show

# Mostrar dependências em árvore
poetry show --tree

# Verificar ambiente
poetry env info

# Remover ambiente virtual
poetry env remove python3.8
```

### Django

```bash
# Criar nova app
poetry run python manage.py startapp nova_app

# Fazer migrações
poetry run python manage.py makemigrations
poetry run python manage.py migrate

# Criar superusuário
poetry run python manage.py createsuperuser

# Shell do Django
poetry run python manage.py shell
```

### Git

```bash
# Verificar status
git status

# Adicionar arquivos
git add .

# Commit (vai executar pre-commit hooks)
git commit -m "feat: adicionar nova funcionalidade"

# Push
git push origin main
```

## 🐛 Troubleshooting

### Problemas Comuns

#### 1. Dependências não instaladas
```bash
# Reinstalar dependências
poetry install --with dev

# Limpar cache
poetry cache clear --all pypi
```

#### 2. Ambiente virtual não ativado
```bash
# Ativar ambiente
poetry shell

# Ou prefixar comandos
poetry run python manage.py runserver
```

#### 3. Conflitos de versão
```bash
# Verificar conflitos
poetry check

# Resolver conflitos manualmente no pyproject.toml
poetry update
```

#### 4. Pre-commit hooks falhando
```bash
# Executar manualmente
poetry run pre-commit run --all-files

# Pular hooks (não recomendado)
git commit -m "feat: ..." --no-verify
```

## 📚 Recursos Adicionais

- [Documentação Poetry](https://python-poetry.org/docs/)
- [Documentação Django](https://docs.djangoproject.com/)
- [Black Code Style](https://black.readthedocs.io/)
- [Ruff Linter](https://beta.ruff.rs/docs/)
- [Pre-commit Hooks](https://pre-commit.com/)

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Faça suas mudanças
4. Execute os testes: `poetry run pytest`
5. Formate o código: `poetry run black src/ && poetry run isort src/`
6. Commit suas mudanças: `git commit -m 'feat: adicionar nova funcionalidade'`
7. Push para a branch: `git push origin feature/nova-funcionalidade`
8. Abra um Pull Request
