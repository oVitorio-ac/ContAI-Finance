# 📚 Documentação ContAI Finance

Bem-vindo à documentação completa do projeto ContAI Finance! Esta pasta centraliza toda a documentação técnica do projeto.

## 📋 Índice da Documentação

### 🏗️ Arquitetura
- **[architecture-diagram.drawio](architecture/architecture-diagram.drawio)** - Diagrama de arquitetura em formato DrawIO
- **[architecture-mermaid.md](architecture/architecture-mermaid.md)** - Diagramas de arquitetura em Mermaid
- **[technical-documentation.md](architecture/technical-documentation.md)** - Documentação técnica completa

### 🧪 Testes
- **[testing.md](development/testing.md)** - Documentação completa dos testes automatizados

### 💰 Custos AWS
- **[aws-cost-analysis.md](cost/aws-cost-analysis.md)** - Análise detalhada de custos por serviço
- **[cost-summary.md](cost/cost-summary.md)** - Resumo executivo e ROI

### 🔌 APIs
- **[api-documentation.md](api/api-documentation.md)** - Documentação completa da API REST

### 📝 Histórico
- **[CHANGELOG.md](CHANGELOG.md)** - Histórico completo de mudanças e versões
- **[prompts-amazon-q-developer.md](development/prompts-amazon-q-developer.md)** - Prompts utilizados com Amazon Q Developer

## 🚀 Links Rápidos

### Para Desenvolvedores
- [Guia de Desenvolvimento](development/development.md) - Configuração completa com Poetry
- [Estrutura do Projeto](architecture/technical-documentation.md#-estrutura-do-projeto)
- [Modelos de Dados](architecture/technical-documentation.md#-modelos-de-dados)
- [APIs e Endpoints](architecture/technical-documentation.md#-apis-e-endpoints)
- [Configurações](architecture/technical-documentation.md#-configurações-de-desenvolvimento)

### Para DevOps
- [Deploy e Infraestrutura](architecture/technical-documentation.md#-deploy-e-infraestrutura)
- [Segurança](architecture/technical-documentation.md#-segurança)
- [Monitoramento](architecture/technical-documentation.md#-monitoramento-e-logs)
- [Custos AWS](cost/aws-cost-analysis.md) - Análise completa
- [ROI e Resumo](cost/cost-summary.md) - Visão executiva

### Para QA
- [Executar Testes](development/testing.md#-executando-os-testes)
- [Estrutura dos Testes](development/testing.md#-estrutura-dos-testes)
- [Cobertura](development/testing.md#-cobertura-de-testes)

### Para Todos
- [Histórico de Mudanças](CHANGELOG.md) - Versões e mudanças
- [Prompts Amazon Q Developer](development/prompts-amazon-q-developer.md) - Interações com IA

## 🎯 Visão Geral do Projeto

ContAI Finance é uma aplicação Django para contadores fazerem upload de arquivos CSV e interagirem com um assistente de IA para análise de dados financeiros.

### Tecnologias Principais
- **Backend**: Django 5.2.6
- **Frontend**: Bootstrap 5
- **Database**: SQLite
- **Tests**: pytest
- **AI**: AWS Bedrock
- **Infrastructure**: Terraform + Docker

### Status do Projeto
- ✅ **Etapa 1**: Projeto base implementado
- ✅ **Etapa 2**: Arquitetura documentada + Testes automatizados
- 🔄 **Etapa 3**: Deploy AWS (em planejamento)

## 📊 Métricas do Projeto

| Métrica | Valor |
|---------|-------|
| Testes Automatizados | 19 testes |
| Cobertura de Código | ~90% |
| Componentes Documentados | 100% |
| Diagramas de Arquitetura | 2 formatos |

## 🔗 Links Externos

- [Repositório GitHub](https://github.com/seu-usuario/ContAI-Finance)
- [Django Documentation](https://docs.djangoproject.com/)
- [AWS Bedrock Docs](https://docs.aws.amazon.com/bedrock/)
- [pytest Documentation](https://docs.pytest.org/)

## 🤝 Contribuindo

Para contribuir com a documentação:

1. Mantenha a estrutura existente
2. Use markdown para formatação
3. Inclua exemplos práticos
4. Atualize este índice quando adicionar novos documentos
5. Teste os exemplos de código antes de commitar

---

**Última atualização**: Janeiro 2024  
**Versão da documentação**: 2.0  
**Projeto**: ContAI Finance - TDC 2025 Q Developer Quest