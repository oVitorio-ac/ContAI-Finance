# 📋 API Documentation - ContAI Finance

## Overview

The ContAI Finance API is a Django-based service that enables CSV file uploads and interaction with an AI assistant for financial data analysis.

**Base URL:** `http://localhost:8000/` (Development)

**Response Format:** JSON

**Authentication:** None (for development)

---

## 📚 Endpoints

### 1. File Upload

#### `GET /`
Loads the upload page containing the file upload form.

**Response (HTML):**
```html
<!-- HTML page with upload form -->
```

#### `POST /`
Processes the upload of a CSV file.

**Form Parameters:**
```json
{
  "titulo": "string",      // Descriptive title of the file
  "arquivo": "file"        // CSV file to be uploaded
}
```

**Success Response (302):**
```text
HTTP 302 Found
Location: /chat/
```

**Error Response (400):**
```json
{
  "error": "Invalid form"
}
```

---

### 2. Chat Interface

#### `GET /chat/`
Loads the chat page with a list of available files.

**Response (HTML):**
```html
<!-- HTML page with chat interface and file list -->
```

**Available Files:**
```json
{
  "arquivos": [
    "finance.csv",
    "financial_data.csv"
  ]
}
```

#### `POST /chat/`
Processes questions about CSV files using AI.

**Form Parameters:**
```json
{
  "pergunta": "string",     // User's question
  "arquivo": "string"       // CSV filename
}
```

**Example Questions:**
- "What is the total revenue?"
- "Provide a full analysis"
- "What are the largest expenses?"
- "Generate automatic insights"

**Success Response (200):**
```json
{
  "resposta": "📊 Analysis of file finance.csv:\n📈 Dimensions: 100 rows, 5 columns\n📋 Columns: Date, Description, Amount, Type\n\n💰 Financial Analysis:\n• Amount: Total R$ 15,000.00, Average R$ 150.00\n  Positives: 60, Negatives: 40"
}
```

**Error Response (500):**
```json
{
  "resposta": "Error processing: [error message]"
}
```

---

### 3. Test Endpoint

#### `GET /test/`
Verifies if the server is running (GET).

**Response (200):**
```json
{
  "status": "GET working",
  "method": "GET"
}
```

#### `POST /test/`
Verifies if the server is running (POST).

**Parameters:**
```json
{
  "any_field": "any_value"
}
```

**Response (200):**
```json
{
  "status": "POST working",
  "data": {
    "field1": ["value1"],
    "field2": ["value2"]
  }
}
```

---

### 4. Debug Endpoint

#### `GET /debug/`
Debug endpoint for development.

**Response (200):**
```json
{
  "method": "GET",
  "status": "OK",
  "data": null
}
```

#### `POST /debug/`
Debug endpoint for development.

**Parameters:**
```json
{
  "any_field": "any_value"
}
```

**Response (200):**
```json
{
  "method": "POST",
  "status": "OK",
  "data": {
    "field1": ["value1"]
  }
}
```

---

## 🔧 API Features

### CSV Analysis
- **Full Analysis**: General file statistics.
- **Specific Queries**: Totals, averages, maximums, minimums.
- **Financial Analysis**: Positive/Negative values.
- **Automatic Insights**: Using AWS Bedrock.

### Supported Question Types
- `analysis` - Full file analysis.
- `total` - Total calculation per column.
- `average` - Average calculation per column.
- `insights` - Generate AI-driven insights.
- Natural language queries interpreted by the system.

---

## 📊 Data Models

### UploadArquivo
```json
{
  "id": "integer",           // Unique ID
  "titulo": "string",        // File title
  "arquivo": "string",       // File path
  "data_upload": "datetime"  // Upload date
}
```

### Analysis Response
```json
{
  "filename": "string",
  "shape": {
    "rows": "integer",
    "columns": "integer"
  },
  "columns": ["string"],
  "value_columns": ["string"],
  "amount_analysis": {
    "total": "float",
    "average": "float",
    "positive_count": "integer",
    "negative_count": "integer"
  }
}
```

---

## ⚠️ Error Handling

### HTTP Status Codes
- `200` - Success
- `302` - Redirect (after upload)
- `400` - Invalid data
- `404` - Resource not found
- `500` - Internal Server Error

### Error Structure
```json
{
  "error": "Descriptive error message",
  "details": "Additional info (optional)"
}
```

### Common Errors
- **File not found**: Ensure a file was selected.
- **Invalid format**: File must be a valid CSV.
- **Processing error**: Issue during file analysis.
- **AI error**: Issue with AWS Bedrock integration.

---

## 🔒 Security

### Implemented Measures
- **CSRF Protection**: Enabled for forms.
- **File Upload Validation**: Type and size validation.
- **SQL Injection Protection**: Django ORM.
- **XSS Protection**: Secure templates.

### Security Settings
```python
# settings.py
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

---

## 📈 Limits and Restrictions

### File Uploads
- **Maximum size**: 10MB per file.
- **Accepted formats**: CSV only.
- **Encoding**: UTF-8 recommended.

### Rate Limiting
- Not implemented (Development).
- Recommended for production.

### Timeout
- **CSV Analysis**: Maximum 30 seconds.
- **Bedrock AI**: Maximum 60 seconds.

---

## 🧪 API Testing

### Unit Tests
```bash
# Test specific endpoints
pytest tests/test_views.py::TestUploadView::test_upload_view_get
pytest tests/test_views.py::TestChatView::test_chat_view_post_valido
```

### Integration Tests
```bash
# Test full workflows
pytest tests/test_e2e.py::TestE2E::test_fluxo_upload_e_chat_completo
```

### E2E Tests
```bash
# Run all E2E tests
pytest -m e2e
```

---

## 🚀 Usage Examples

### Python (requests)
```python
import requests

# File upload
files = {'arquivo': open('data.csv', 'rb')}
data = {'titulo': 'Financial Data'}
response = requests.post('http://localhost:8000/', files=files, data=data)

# Ask question
data = {
    'pergunta': 'What is the total revenue?',
    'arquivo': 'data.csv'
}
response = requests.post('http://localhost:8000/chat/', data=data)
print(response.json())
```

### cURL
```bash
# Upload
curl -X POST http://localhost:8000/ \
  -F "titulo=Financial Data" \
  -F "arquivo=@data.csv"

# Chat
curl -X POST http://localhost:8000/chat/ \
  -d "pergunta=What is the total?&arquivo=data.csv"
```

---

## 📝 Development Notes

- **CSRF Exempt**: Some endpoints use `@csrf_exempt` for easier testing.
- **CORS**: Not configured (local development).
- **Logging**: All requests are logged.
- **Debug Mode**: Debug settings enabled.

---

**Last Update:** January 2026
**API Version:** 1.0
**Status:** Development