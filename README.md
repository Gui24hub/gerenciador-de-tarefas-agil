# Gerenciador de Tarefas Ágil

Este projeto simula um sistema simples de gerenciamento de tarefas baseado em metodologias ágeis, permitindo criar, listar, atualizar e remover tarefas.

## 🎯 Objetivo

Demonstrar na prática:
- Planejamento e execução de um projeto de software ágil
- Organização de tarefas com Kanban
- Versionamento e colaboração com Git e GitHub
- Implementação de um CRUD funcional utilizando Python + Flask
- Controle de qualidade com testes automatizados
- Integração Contínua com GitHub Actions
- Registro de **gestão de mudanças** no desenvolvimento## 🚀 Como Executar o Projeto

### 1. Instalar dependências

pip install flask
pip install pytest


### 2. Executar o sistema

python src/app.py

### 3. Acessar no navegador

http://127.0.0.1:5000/tarefas

### 4. Rodar os testes

pytest

## 🛠️ Tecnologias Utilizadas

| Componente | Ferramenta |
|-----------|------------|
| Linguagem | Python 3.x |
| Framework Web | Flask |
| Testes Automatizados | PyTest |
| Integração Contínua | GitHub Actions |
| Versionamento | Git + GitHub |
| Diagramas UML | Mermaid / PNG |
| Editor Sugerido | VS Code ou Spyder |

## ✨ Funcionalidades do Sistema

| Função | Descrição | Rota | Método |
|-------|-----------|------|--------|
| Criar tarefa | Adiciona uma nova tarefa | `/tarefas` | POST |
| Listar tarefas | Exibe todas as tarefas registradas | `/tarefas` | GET |
| Atualizar tarefa | Edita título, descrição, status e prioridade | `/tarefas/<id>` | PUT |
| Remover tarefa | Exclui tarefa da lista | `/tarefas/<id>` | DELETE |

## 🛠️ Metodologia
Foi utilizado Kanban através da aba Projects do GitHub, com fluxo:


## 🔄 Mudança de Escopo (Será adicionada depois)

Inicialmente, o sistema possuía apenas os atributos básicos de uma tarefa.  
Após análise, identificou-se a necessidade de permitir ao **Gestor priorizar tarefas**, para facilitar o planejamento e tomada de decisão.

Foi adicionada a propriedade `prioridade`, que pode assumir valores:
- Alta
- Média (padrão)
- Baixa

A mudança foi refletida:
- No código (CRUD)
- No Diagrama de Classes
- No Kanban do GitHub Projects

## 📂 Estrutura do Repositório

gerenciador-de-tarefas-agil
│
├── README.md # Documentação
├── docs/ # Diagramas e arquivos de apoio
│ ├── diagrama-casos-uso.png
│ └── diagrama-classes.png
│
├── src/ # Código do sistema
│ └── app.py
│
├── tests/ # Testes automatizados
│ └── test_tarefas.py
│
└── .github/workflows/ # Pipeline CI
└── python-tests.yml


# 🔄 Mudança de Escopo (Feature Adicionada)

Durante o desenvolvimento, percebeu-se a necessidade de permitir ao **Gestor** identificar quais tarefas são mais urgentes.  
Com isso, foi adicionada a propriedade:

prioridade = Alta | Média (padrão) | Baixa

yaml
Copy code

Essa mudança foi aplicada em:
- Código
- Diagrama de Classes
- Documentação
- Kanban do GitHub Projects

---

## 🗂️ Gestão Ágil no GitHub (Kanban)

Foi utilizado o **GitHub Projects**, organizado com três colunas:

To Do → In Progress → Done

yaml
Copy code

Cada atividade foi criada como um card e movida conforme progresso, garantindo transparência e acompanhamento do desenvolvimento.

---

## ✅ Controle de Qualidade (CI/CD)

O repositório possui um **pipeline configurado** com GitHub Actions que:
- Instala dependências automaticamente
- Executa testes a cada *commit*
- Garante que o projeto não seja enviado com erros

Arquivo responsável:
.github/workflows/python-tests.yml

yaml
Copy code

---

## 🧩 Diagramas UML

### Diagrama de Caso de Uso
Local: `docs/diagrama-casos-uso.png`

### Diagrama de Classes
Local: `docs/diagrama-classes.png`


##  👤 Autor: Guilherme M

Projeto desenvolvido para fins acadêmicos


