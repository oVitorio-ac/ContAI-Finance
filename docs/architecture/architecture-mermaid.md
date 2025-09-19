# Diagrama de Arquitetura - ContAI Finance

## Arquitetura Geral

```mermaid
graph TB
    subgraph "Frontend Layer"
        U[👤 Contador] --> F[🌐 Frontend<br/>Bootstrap + HTML]
    end
    
    subgraph "Application Layer"
        F --> D[🐍 Django Application<br/>Views + Models + Forms]
    end
    
    subgraph "Data Layer"
        D --> DB[(🗄️ SQLite Database<br/>UploadArquivo Model)]
        D --> FS[📁 Media Storage<br/>CSV Files]
    end
    
    subgraph "MCP Servers"
        D --> MCP1[🔍 CSV Analyzer<br/>MCP Server]
        D --> MCP2[🤖 Bedrock Integration<br/>MCP Server]
    end
    
    subgraph "AWS Services"
        MCP1 --> FS
        MCP2 --> AWS1[🧠 AWS Bedrock<br/>AI Analysis]
        FS -.-> AWS2[☁️ AWS S3<br/>Future Integration]
    end
    
    subgraph "Infrastructure"
        D -.-> DOCKER[🐳 Docker<br/>Containerization]
        DOCKER -.-> TERRA[🏗️ Terraform IaC<br/>ECS + Lambda + ALB]
    end
    
    classDef implemented fill:#d5e8d4,stroke:#82b366
    classDef future fill:#fff2cc,stroke:#d6b656,stroke-dasharray: 5 5
    classDef aws fill:#ff9999,stroke:#d79b00
    
    class U,F,D,DB,FS,MCP1,MCP2,AWS1 implemented
    class AWS2,DOCKER,TERRA future
```

## Fluxo de Dados

```mermaid
sequenceDiagram
    participant C as 👤 Contador
    participant F as 🌐 Frontend
    participant D as 🐍 Django
    participant DB as 🗄️ Database
    participant FS as 📁 Storage
    participant MCP as 🔍 CSV Analyzer
    participant BR as 🧠 Bedrock
    
    C->>F: 1. Upload CSV
    F->>D: 2. POST /upload
    D->>DB: 3. Save metadata
    D->>FS: 4. Store file
    D->>F: 5. Redirect to chat
    
    C->>F: 6. Ask question
    F->>D: 7. POST /chat
    D->>MCP: 8. Analyze CSV
    MCP->>FS: 9. Read file
    MCP->>D: 10. Return analysis
    
    alt Advanced Analysis
        D->>BR: 11. Request insights
        BR->>D: 12. AI response
    end
    
    D->>F: 13. JSON response
    F->>C: 14. Display answer
```

## Componentes Principais

### 1. Frontend
- **Bootstrap 5** para UI responsiva
- **HTML5** templates com Django
- **JavaScript** para interações AJAX

### 2. Backend
- **Django 5.2.6** framework web
- **SQLite** banco de dados local
- **Boto3** para integração AWS (futuro)

### 3. MCP Servers
- **CSV Analyzer**: Análise local de arquivos CSV
- **Bedrock Integration**: IA para insights avançados

### 4. Infraestrutura (Planejada)
- **Docker** para containerização
- **Terraform** para IaC na AWS
- **ECS Fargate** para deploy
- **S3** para armazenamento de arquivos
- **Lambda** para processamento serverless

## Tecnologias Utilizadas

| Componente | Tecnologia | Status |
|------------|------------|--------|
| Frontend | Bootstrap 5, HTML5, JS | ✅ Implementado |
| Backend | Django 5.2.6, Python 3.8+ | ✅ Implementado |
| Database | SQLite | ✅ Implementado |
| Storage | Local Media | ✅ Implementado |
| MCP | CSV Analyzer | ✅ Implementado |
| AI | AWS Bedrock | ✅ Implementado |
| Container | Docker | 🔄 Planejado |
| Cloud | AWS S3, ECS, Lambda | 🔄 Planejado |
| IaC | Terraform | 🔄 Planejado |