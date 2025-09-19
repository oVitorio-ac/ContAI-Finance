# ContAI Finance - Configuração Amazon Q Developer

## Visão Geral do Projeto
Aplicação Django para contadores analisarem dados financeiros via CSV com assistente de IA integrado.

## Arquitetura
- **Backend**: Django 5.2.6 com SQLite
- **Frontend**: Bootstrap 5 + HTML5
- **MCP Server**: Análise de CSV com pandas
- **Cloud**: AWS (S3, Lambda, ECS)

## Estrutura de Diretórios
```
ContAI-Finance/
├── contai_finance/          # Configurações Django
├── financeiro/              # App principal
├── mcp_server/              # Servidor MCP para análise CSV
├── infrastructure/          # IaC (Terraform)
├── templates/               # Templates HTML
├── static/                  # Arquivos estáticos
├── media/uploads/           # CSVs enviados
├── tests/                   # Testes automatizados
└── docs/                    # Documentação
```

## Funcionalidades Principais
1. **Upload de CSV**: Usuários fazem upload de arquivos financeiros
2. **Análise via MCP**: Servidor MCP processa e analisa dados
3. **Chat com IA**: Interface para perguntas sobre os dados
4. **Deploy AWS**: Infraestrutura completa na AWS

## Tecnologias
- Django, pandas, boto3
- Bootstrap, JavaScript
- Terraform (IaC)
- Amazon S3, ECS, Lambda

## Comandos Úteis
```bash
# Desenvolvimento
python manage.py runserver
python manage.py test

# Deploy
cd infrastructure
terraform init
terraform plan
terraform apply
```

## Padrões de Código
- Views baseadas em função
- Templates com herança
- Testes unitários e E2E
- Documentação inline
- Tratamento de erros