# 📋 Documentação da API - ContAI Finance

## Visão Geral

A API do ContAI Finance é uma aplicação Django RESTful que permite upload de arquivos CSV e interação com assistente de IA para análise de dados financeiros.

**Base URL:** `http://localhost:8000/` (desenvolvimento)

**Formato de Resposta:** JSON

**Autenticação:** Nenhuma (para desenvolvimento)

---

## 📚 Endpoints

### 1. Upload de Arquivos

#### `GET /`
Carrega a página de upload com formulário.

**Resposta (HTML):**
```html
<!-- Página HTML com formulário de upload -->
```

#### `POST /`
Processa o upload de arquivo CSV.

**Parâmetros do Formulário:**
```json
{
  "titulo": "string",      // Título descritivo do arquivo
  "arquivo": "file"        // Arquivo CSV a ser enviado
}
```

**Resposta de Sucesso (302):**
```
HTTP 302 Found
Location: /chat/
```

**Resposta de Erro (400):**
```json
{
  "error": "Formulário inválido"
}
```

---

### 2. Interface de Chat

#### `GET /chat/`
Carrega a página de chat com lista de arquivos disponíveis.

**Resposta (HTML):**
```html
<!-- Página HTML com interface de chat e lista de arquivos -->
```

**Arquivos Disponíveis:**
```json
{
  "arquivos": [
    "financeiro.csv",
    "dados_financeiros.csv"
  ]
}
```

#### `POST /chat/`
Processa perguntas sobre arquivos CSV usando IA.

**Parâmetros do Formulário:**
```json
{
  "pergunta": "string",     // Pergunta do usuário
  "arquivo": "string"       // Nome do arquivo CSV
}
```

**Exemplos de Perguntas:**
- "Qual é o total de receitas?"
- "Faça uma análise completa"
- "Quais são as maiores despesas?"
- "Gere insights automáticos"

**Resposta de Sucesso (200):**
```json
{
  "resposta": "📊 Análise do arquivo financeiro.csv:\n📈 Dimensões: 100 linhas, 5 colunas\n📋 Colunas: Data, Descrição, Valor, Tipo\n\n💰 Análise Financeira:\n• Valor: Total R$ 15.000,00, Média R$ 150,00\n  Positivos: 60, Negativos: 40"
}
```

**Resposta de Erro (500):**
```json
{
  "resposta": "Erro ao processar: [mensagem de erro]"
}
```

---

### 3. Endpoint de Teste

#### `GET /test/`
Verifica se o servidor está funcionando (GET).

**Resposta (200):**
```json
{
  "status": "GET funcionando",
  "method": "GET"
}
```

#### `POST /test/`
Verifica se o servidor está funcionando (POST).

**Parâmetros:**
```json
{
  "qualquer_campo": "qualquer_valor"
}
```

**Resposta (200):**
```json
{
  "status": "POST funcionando",
  "data": {
    "campo1": ["valor1"],
    "campo2": ["valor2"]
  }
}
```

---

### 4. Endpoint de Debug

#### `GET /debug/`
Endpoint de debug para desenvolvimento.

**Resposta (200):**
```json
{
  "method": "GET",
  "status": "OK",
  "data": null
}
```

#### `POST /debug/`
Endpoint de debug para desenvolvimento.

**Parâmetros:**
```json
{
  "qualquer_campo": "qualquer_valor"
}
```

**Resposta (200):**
```json
{
  "method": "POST",
  "status": "OK",
  "data": {
    "campo1": ["valor1"]
  }
}
```

---

## 🔧 Funcionalidades da API

### Análise de CSV
- **Análise completa**: Estatísticas gerais do arquivo
- **Consultas específicas**: Totais, médias, máximos, mínimos
- **Análise financeira**: Valores positivos/negativos
- **Insights automáticos**: Usando AWS Bedrock

### Tipos de Perguntas Suportadas
- `análise` - Análise completa do arquivo
- `total` - Cálculo de totais por coluna
- `média` - Cálculo de médias por coluna
- `insights` - Geração de insights com IA
- Consultas livres interpretadas pelo sistema

---

## 📊 Modelos de Dados

### UploadArquivo
```python
{
  "id": "integer",           // ID único
  "titulo": "string",        // Título do arquivo
  "arquivo": "string",       // Caminho do arquivo
  "data_upload": "datetime"  // Data de upload
}
```

### Resposta de Análise
```json
{
  "filename": "string",
  "shape": {
    "rows": "integer",
    "columns": "integer"
  },
  "columns": ["string"],
  "value_columns": ["string"],
  "valor_analysis": {
    "total": "float",
    "average": "float",
    "positive_count": "integer",
    "negative_count": "integer"
  }
}
```

---

## ⚠️ Tratamento de Erros

### Códigos de Status HTTP
- `200` - Sucesso
- `302` - Redirecionamento (após upload)
- `400` - Dados inválidos
- `404` - Recurso não encontrado
- `500` - Erro interno do servidor

### Estrutura de Erro
```json
{
  "error": "Mensagem descritiva do erro",
  "details": "Informações adicionais (opcional)"
}
```

### Erros Comuns
- **Arquivo não encontrado**: Verifique se o arquivo foi selecionado
- **Formato inválido**: Arquivo deve ser CSV válido
- **Erro de processamento**: Problema na análise do arquivo
- **Erro de IA**: Problema na integração com AWS Bedrock

---

## 🔒 Segurança

### Medidas Implementadas
- **CSRF Protection**: Habilitado para formulários
- **File Upload Validation**: Validação de tipos e tamanhos
- **SQL Injection Protection**: ORM Django
- **XSS Protection**: Templates seguros

### Configurações de Segurança
```python
# settings.py
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

---

## 📈 Limites e Restrições

### Upload de Arquivos
- **Tamanho máximo**: 10MB por arquivo
- **Formatos aceitos**: CSV apenas
- **Encoding**: UTF-8 recomendado

### Rate Limiting
- Não implementado (desenvolvimento)
- Recomendado para produção

### Timeout
- **Análise CSV**: Máximo 30 segundos
- **Bedrock IA**: Máximo 60 segundos

---

## 🧪 Testes da API

### Testes Unitários
```bash
# Testar endpoints específicos
pytest tests/test_views.py::TestUploadView::test_upload_view_get
pytest tests/test_views.py::TestChatView::test_chat_view_post_valido
```

### Testes de Integração
```bash
# Testar fluxos completos
pytest tests/test_e2e.py::TestE2E::test_fluxo_upload_e_chat_completo
```

### Testes E2E
```bash
# Executar todos os testes E2E
pytest -m e2e
```

---

## 🚀 Exemplos de Uso

### Python (requests)
```python
import requests

# Upload de arquivo
files = {'arquivo': open('dados.csv', 'rb')}
data = {'titulo': 'Dados Financeiros'}
response = requests.post('http://localhost:8000/', files=files, data=data)

# Fazer pergunta
data = {
    'pergunta': 'Qual é o total de receitas?',
    'arquivo': 'dados.csv'
}
response = requests.post('http://localhost:8000/chat/', data=data)
print(response.json())
```

### cURL
```bash
# Upload
curl -X POST http://localhost:8000/ \
  -F "titulo=Dados Financeiros" \
  -F "arquivo=@dados.csv"

# Chat
curl -X POST http://localhost:8000/chat/ \
  -d "pergunta=Qual é o total?&arquivo=dados.csv"
```

---

## 📝 Notas de Desenvolvimento

- **CSRF Exempt**: Alguns endpoints usam `@csrf_exempt` para facilitar testes
- **CORS**: Não configurado (desenvolvimento local)
- **Logging**: Todos os requests são logados
- **Debug Mode**: Configurações de debug habilitadas

---

**Última atualização:** Janeiro 2024
**Versão da API:** 1.0
**Status:** Desenvolvimento