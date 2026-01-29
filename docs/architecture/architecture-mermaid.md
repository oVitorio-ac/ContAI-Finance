# Architecture Diagram - ContAI Finance

## General Architecture

```mermaid
graph TB
    subgraph "Frontend Layer"
        U[👤 Accountant] --> F[🌐 Frontend<br/>Bootstrap + HTML]
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

## Data Flow

```mermaid
sequenceDiagram
    participant C as 👤 Accountant
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

## Main Components

### 1. Frontend
- **Bootstrap 5** for responsive UI.
- **HTML5** templates with Django.
- **JavaScript** for AJAX interactions.

### 2. Backend
- **Django 5.2.6** web framework.
- **SQLite** local database.
- **Boto3** for AWS integration (future).

### 3. MCP Servers
- **CSV Analyzer**: Local analysis of CSV files.
- **Bedrock Integration**: AI for advanced insights.

### 4. Infrastructure (Planned)
- **Docker** for containerization.
- **Terraform** for IaC on AWS.
- **ECS Fargate** for deployment.
- **S3** for file storage.
- **Lambda** for serverless processing.

## Technologies Used

| Component | Technology | Status |
|------------|------------|--------|
| Frontend | Bootstrap 5, HTML5, JS | ✅ Implemented |
| Backend | Django 5.2.6, Python 3.12+ | ✅ Implemented |
| Database | SQLite | ✅ Implemented |
| Storage | Local Media | ✅ Implemented |
| MCP | CSV Analyzer | ✅ Implemented |
| AI | AWS Bedrock | ✅ Implemented |
| Container | Docker | 🔄 Planned |
| Cloud | AWS S3, ECS, Lambda | 🔄 Planned |
| IaC | Terraform | 🔄 Planned |