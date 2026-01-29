# 🤖 Prompts Used with Amazon Q Developer

This document contains the complete history of prompts used during the development of the ContAI Finance project with Amazon Q Developer.

## 📋 Overview

The prompts are organized by development tiers, following the TDC 2025 - Q Developer Quest structure. Each prompt represents a specific interaction with the AI assistant during project implementation.

## 🔄 Development Tiers

### Tier 1 - Initial Configuration

#### Prompt 1: Running the Project
```text
i need help for run my project
```
**Context**: Initial request for assistance in running the Django project.

#### Prompt 2: Resolving Runtime Errors
```text
ok , my project is ruuning now . but very much error . why?
```
**Context**: After attempting to run the project, multiple errors appeared and needed to be diagnosed.

#### Prompt 3: ALLOWED_HOSTS Issue
```text
Invalid HTTP_HOST header: 'd3vq5f4ity3pv8.cloudfront.net'. You may need to add 'd3vq5f4ity3pv8.cloudfront.net' to ALLOWED_HOSTS.
```
**Context**: Specific error related to the configuration of allowed hosts in Django.

#### Prompt 4: Centralized Frontend Layout
```text
no front pode deixar tudo centralizado na tela
```
(Translation: "In the frontend, can you center everything on the screen?")
**Context**: Request to improve the user interface layout by centering elements on the screen.

#### Prompt 5: Tier 1 Verification
```text
etapa 1 do projeto essa que fizemos ?
```
(Translation: "Is this Tier 1 of the project that we completed?")
**Context**: Confirmation of progress regarding Tier 1 of the project.

### Tier 2 - Architecture and Testing

#### Prompt 6: Full Tier 2 Implementation
```text
pode me ajudar a montar isso Etapa 2: Mochilinha exclusiva AWS Tudo da Etapa 1 Diagrama de arquitetura (drawio, mermaid, etc...) Um ou mais testes automatizados (unidade, integração, E2E) e coloca na pasta docs por favor e analiza o que eu pensei e ve se faz sentido para esse projeto
```
(Translation: "Can you help me set this up: Tier 2. Everything from Tier 1, Architecture Diagram (drawio, mermaid, etc...), one or more automated tests (unit, integration, E2E), put it in the docs folder please, analyze my idea and see if it makes sense for this project.")
**Context**: Comprehensive request to implement all of Tier 2, including architecture and testing.

#### Prompt 7: Chat Route Issue
```text
bom nao consigo acessa rota do chat?
```
(Translation: "Well, I can't access the chat route?")
**Context**: Difficulty in accessing the application's chat route.

#### Prompt 8: Centralized Diagrams and Tests
```text
pode fazer o seguinte diagrama para o formato do drawio e usa o pytest para os teste automatizados centraliza toda a documentação do projeto na pasta docs E gera o readme
```
(Translation: "Can you make the following diagram in DrawIO format, use pytest for automated tests, centralize all project documentation in the docs folder, and generate the readme.")
**Context**: Request to create DrawIO diagrams, implement tests with pytest, centralize documentation, and generate the README.

## ✅ Implemented Solutions

### Technical Fixes
- ✅ **Missing Directories**: Created `static/` and `media/` folders.
- ✅ **Database Migrations**: Correct configuration of SQLite.
- ✅ **URLs and Redirects**: Adjusted application routes.
- ✅ **Centralized Layout**: Improved frontend interface.

### Documentation and Architecture
- ✅ **Mermaid Diagrams**: Visual architecture diagrams.
- ✅ **Test Suite**: 19 automated tests with pytest.
- ✅ **Technical Documentation**: Centralized in the `docs/` folder.
- ✅ **Updated README**: Included screenshots and instructions.

## 📊 Prompt Statistics

| Tier | Number of Prompts | Main Focus |
|-------|------------------|----------------|
| **Tier 1** | 5 prompts | Initial setup and basic fixes |
| **Tier 2** | 3 prompts | Architecture, testing, and documentation |
| **Total** | 8 prompts | Full project development |

## 🎯 Observed Patterns

### Types of Prompts Used
1. **Problem Diagnosis**: Identifying and resolving errors.
2. **Functional Requests**: Implementing new features.
3. **UX Improvements**: Adjustments to the user interface.
4. **Documentation**: Creating diagrams and technical documentation.
5. **Testing**: Implementing automated tests.

### Effective Strategies
- **Specific Prompts**: Detailed descriptions of the problem.
- **Context Provided**: Information about the current state.
- **Clear Objectives**: Well-defined expected results.
- **Progressive Iteration**: Incremental development.

## 🔗 Relations to Other Documents

- **[CHANGELOG.md](CHANGELOG.md)**: History of implemented changes.
- **[technical-documentation.md](technical-documentation.md)**: Detailed technical documentation.
- **[testing.md](testing.md)**: Comprehensive test documentation.
- **[architecture-mermaid.md](architecture-mermaid.md)**: Architecture diagrams.

## 📝 Development Notes

This history demonstrates how Amazon Q Developer was utilized strategically throughout the entire development cycle, from initial setup to the full implementation of features and documentation.

---