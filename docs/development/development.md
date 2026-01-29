# 🛠️ Development Guide - ContAI Finance

This document contains detailed instructions for setting up and working on the project using Poetry.

## 📋 Prerequisites

- **Python 3.12+**
- **Poetry** (package manager)
- **Git**

## 🚀 Initial Setup

### 1. Install Poetry

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Verify installation
poetry --version
```

### 2. Clone and Configure Project

```bash
# Clone the repository
git clone https://github.com/oVitorio-ac/ContAI-Finance.git
cd ContAI-Finance

# Install development dependencies
poetry install

# Activate the Poetry shell (optional)
poetry shell
```

### 3. Environment Configuration

```bash
# Copy the example environment variables file
cp .env.example .env

# Edit .env with your settings
nano .env
```

### 4. Configure Pre-commit Hooks

```bash
# Install hooks
poetry run pre-commit install

# Run hooks on all files
poetry run pre-commit run --all-files
```

## 🏃‍♂️ Running the Project

### Local Development

```bash
# Run migrations
poetry run python manage.py migrate

# Create a superuser (optional)
poetry run python manage.py createsuperuser

# Start the development server
poetry run python manage.py runserver
```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=src --cov-report=html

# Run tests by category
poetry run pytest -m unit        # Unit tests
poetry run pytest -m integration # Integration tests
poetry run pytest -m e2e         # End-to-end tests

# Run specific tests
poetry run pytest tests/test_models.py
poetry run pytest tests/test_views.py::TestViews::test_upload_view_get
```

## 🛠️ Development Tools

### Formatting and Linting

```bash
# Format code with Black
poetry run black src/

# Organize imports with isort
poetry run isort src/

# Linting with Ruff
poetry run ruff check src/
poetry run ruff format src/

# Auto-fix linting issues
poetry run ruff check src/ --fix
```

### Security Verification

```bash
# Check for vulnerabilities
poetry run safety check

# List licenses
poetry run pip-licenses
```

## 📦 Dependency Management

### Adding Dependencies

```bash
# Main dependency
poetry add requests

# Development dependency
poetry add --group dev pytest-cov

# Production dependency
poetry add --group prod gunicorn
```

### Updating Dependencies

```bash
# Update all dependencies
poetry update

# Update a specific dependency
poetry update requests

# Show outdated dependencies
poetry show --outdated
```

### Exporting Requirements (if needed)

```bash
# For development
poetry export -f requirements.txt --with dev -o requirements-dev.txt

# For production
poetry export -f requirements.txt --only main,prod -o requirements.txt
```

## 🐳 Docker (Optional)

### Building the Image

```bash
# Build the image
docker build -f infrastructure/docker/Dockerfile -t contai-finance .

# Run the container
docker run -p 8000:8000 contai-finance
```

### Using Docker Compose

```bash
# If docker-compose.yml exists
docker-compose up -d
```

## 🚀 Deployment

### Production

```bash
# Install only production dependencies
poetry install --only main,prod

# Collect static files
poetry run python manage.py collectstatic --noinput

# Run migrations
poetry run python manage.py migrate

# Start server with Gunicorn
poetry run gunicorn contai_finance.wsgi:application --bind 0.0.0.0:8000
```

### AWS (Terraform)

```bash
# Initialize Terraform
cd infrastructure/terraform
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply
```

## 🔧 Useful Commands

### Poetry

```bash
# Show project info
poetry show

# Show dependency tree
poetry show --tree

# Verify environment
poetry env info

# Remove virtual environment
poetry env remove python3.12
```

### Django

```bash
# Create a new app
poetry run python manage.py startapp new_app

# Run migrations
poetry run python manage.py makemigrations
poetry run python manage.py migrate

# Create a superuser
poetry run python manage.py createsuperuser

# Django shell
poetry run python manage.py shell
```

### Git

```bash
# Check status
git status

# Add files
git add .

# Commit (will trigger pre-commit hooks)
git commit -m "feat: add new functionality"

# Push
git push origin main
```

## 🐛 Troubleshooting

### Common Problems

#### 1. Dependencies not installed
```bash
# Reinstall dependencies
poetry install

# Clear cache
poetry cache clear --all pypi
```

#### 2. Virtual environment not activated
```bash
# Activate environment
poetry shell

# Or prefix commands
poetry run python manage.py runserver
```

#### 3. Version conflicts
```bash
# Check for conflicts
poetry check

# Resolve conflicts manually in pyproject.toml
poetry update
```

#### 4. Pre-commit hooks failing
```bash
# Run hooks manually
poetry run pre-commit run --all-files

# Skip hooks (not recommended)
git commit -m "feat: ..." --no-verify
```

## 📚 Additional Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Black Code Style](https://black.readthedocs.io/)
- [Ruff Linter](https://docs.astral.sh/ruff/)
- [Pre-commit Hooks](https://pre-commit.com/)

## 🤝 Contributing

1. Fork the project.
2. Create your branch: `git checkout -b feature/new-functionality`
3. Make your changes.
4. Run tests: `poetry run pytest`
5. Format code: `poetry run black src/ && poetry run isort src/`
6. Commit your changes: `git commit -m 'feat: add new functionality'`
7. Push to the branch: `git push origin feature/new-functionality`
8. Open a Pull Request.
