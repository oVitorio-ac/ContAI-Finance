# ContAI Finance

**Projeto desenvolvido para o TDC 2025 - Q Developer Quest**

Uma aplicação Django para contadores fazerem upload de arquivos CSV e interagirem com um assistente de IA.

## 🏷️ Tags
- `q-developer-quest-tdc-2025`
- `django`
- `aws`
- `amazon-q-developer`

## 📸 Screenshots

### Tela de Upload
![Upload Screen](ContAI-Finance/screenshots/upload-screen.png)

### Tela de Chat
![Chat Screen](ContAI-Finance/screenshots/chat-screen.png)

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior
- Git

### Passos de Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/oVitorio-ac/ContAI-Finance.git
   cd ContAI-Finance
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install django boto3
   ```

4. **Execute as migrações**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o servidor**:
   ```bash
   python manage.py runserver
   ```

6. **Acesse a aplicação**:
   - Home/Upload: http://127.0.0.1:8000/
   - Chat: http://127.0.0.1:8000/chat/

## 🤖 Prompts Utilizados com Amazon Q Developer

### Etapa 1 - Configuração Inicial
1. `i need help for run my project`
2. `ok , my project is ruuning now . but very much error . why?`
3. `Invalid HTTP_HOST header: 'd3vq5f4ity3pv8.cloudfront.net'. You may need to add 'd3vq5f4ity3pv8.cloudfront.net' to ALLOWED_HOSTS.`
4. `no front pode deixar tudo centralizado na tela`
5. `etapa 1 do projeto essa que fizemos ?`

### Etapa 2 - Arquitetura e Testes
6. `pode me ajudar a montar isso Etapa 2: Mochilinha exclusiva AWS Tudo da Etapa 1 Diagrama de arquitetura (drawio, mermaid, etc...) Um ou mais testes automatizados (unidade, integração, E2E) e coloca na pasta docs por favor e analiza o que eu pensei e ve se faz sentido para esse projeto`
7. `bom nao consigo acessa rota do chat?`
8. `pode fazer o seguinte diagrama para o formato do drawio e usa o pytest para os teste automatizados centraliza toda a documentação do projeto na pasta docs E gera o readme`

### Soluções Implementadas
- ✅ Correção de diretórios ausentes (static, media)
- ✅ Configuração de migrações do banco
- ✅ Ajuste de URLs e redirecionamentos
- ✅ Centralização do layout
- ✅ Diagramas de arquitetura Mermaid
- ✅ Suite completa de testes automatizados
- ✅ Documentação técnica detalhada

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.6
- **Frontend**: Bootstrap 5, HTML5
- **Banco de Dados**: SQLite
- **Cloud**: AWS (boto3 para integração S3)
- **Desenvolvimento**: Amazon Q Developer

## 📁 Estrutura do Projeto

```
ContAI-Finance/
├── contai_finance/          # Configurações Django
├── financeiro/              # App principal
├── templates/               # Templates HTML
├── static/                  # Arquivos estáticos
├── media/                   # Uploads de arquivos
├── venv/                    # Ambiente virtual
├── manage.py               # Script Django
├── README.md               # Este arquivo
└── requirements.txt        # Dependências
```

## 🎯 Funcionalidades

- ✅ Upload de arquivos CSV
- ✅ Interface de chat com IA
- ✅ Tema escuro responsivo
- ✅ Design centralizado
- ✅ Servidor MCP para análise de CSV
- ✅ Integração AWS Bedrock para insights avançados
- ✅ Análise automática de dados financeiros
- ✅ Deploy completo na AWS (ECS + S3 + Lambda)
- 🔄 Integração com Amazon S3 (infraestrutura pronta)

## 🏆 TDC 2025 - Q Developer Quest

### ✅ Etapa 1 - Bolsinha Cabos Exclusiva AWS
- ✅ Projeto gerado com Amazon Q Developer
- ✅ Projeto público no GitHub com tag `q-developer-quest-tdc-2025`
- ✅ README.md com screenshots
- ✅ Lista dos prompts utilizados

### ✅ Etapa 2 - Mochilinha Exclusiva AWS
- ✅ Tudo da Etapa 1
- ✅ Diagrama de arquitetura (DrawIO + Mermaid)
- ✅ Testes automatizados (19 testes: unitários, integração, E2E)
- ✅ Documentação técnica completa na pasta `docs/`

### ✅ Etapa 2 - Mochilinha Exclusiva AWS
- ✅ Tudo da Etapa 1
- ✅ Diagrama de arquitetura (Mermaid)
- ✅ Testes automatizados (19 testes: unitários, integração, E2E)

### ✅ Etapa 3 - Garrafa + Toalha Exclusiva AWS
- ✅ Tudo das Etapas 1 & 2
- ✅ **3 Servidores MCP integrados**:
  - CSV Analyzer (customizado)
  - AWS Bedrock Data Automation (oficial)
  - AWS Pricing Calculator (oficial)
- ✅ Configuração Amazon Q Developer no repositório
- ✅ IaC completa (Terraform: ECS, S3, Lambda, ALB, VPC)
- ✅ Integração AWS Bedrock para análise avançada de dados
- ✅ **Cálculo de custos em tempo real**
- ✅ Deploy automatizado com Docker + ECS Fargate

## 📊 Arquitetura

Veja a documentação completa da arquitetura em:
- [Diagrama DrawIO](ContAI-Finance/docs/architecture-diagram.drawio) - Formato DrawIO
- [Diagramas Mermaid](ContAI-Finance/docs/architecture-mermaid.md) - Diagramas Mermaid
- [Documentação Técnica](ContAI-Finance/docs/technical-documentation.md) - Documentação completa

## 💰 Custos de Implementação AWS

**Estimativa**: $100-125 USD/mês para 50 usuários

- [Análise Completa de Custos](ContAI-Finance/docs/aws-cost-analysis.md) - Análise detalhada por serviço
- [Resumo Executivo](ContAI-Finance/docs/cost-summary.md) - Visão rápida e ROI
- **ROI**: 80x retorno (economia de $10,000/mês vs custo de $125/mês)

## 🧪 Testes Automatizados

### Executar Todos os Testes
```bash
# Script personalizado
python run_tests.py

# Django diretamente
python manage.py test tests

# Pytest com marcadores
pytest -m unit        # Testes unitários
pytest -m integration # Testes de integração
pytest -m e2e         # Testes E2E
```

### Cobertura de Testes
- **19 testes** implementados com **pytest**
- **Testes Unitários**: Models, Forms (7 testes)
- **Testes de Integração**: Views, URLs (8 testes) 
- **Testes E2E**: Fluxos completos (4 testes)
- **Cobertura**: >90% do código

Veja documentação completa em [docs/testing.md](ContAI-Finance/docs/testing.md)

## 📝 Licença

MIT License - veja o arquivo LICENSE para detalhes.