# SentinelFlow AI

### Autonomous Multi-Agent Enterprise Workflow Orchestrator

---

##  Overview

SentinelFlow AI is an **enterprise-grade multi-agent system** designed to autonomously execute complex business workflows with built-in:

* Self-healing error recovery
* Full auditability
* AI memory & learning
* Workflow monitoring

Unlike traditional automation systems, SentinelFlow AI **does not stop on failure** — it detects issues, adapts, and continues execution intelligently.

---

##  Problem Statement

Enterprise workflows (e.g., vendor payments, onboarding, contract processing) are:

* Fragmented across multiple systems
* Dependent on manual intervention
* Prone to failures and delays

When a single step fails, the entire workflow stops — causing SLA breaches and inefficiency.

---

## Solution

SentinelFlow AI introduces a **multi-agent architecture** where specialized AI agents collaborate to:

* Plan workflows
* Validate actions
* Execute tasks
* Detect and recover from failures
* Learn from past executions

Result: **Autonomous, reliable, and self-improving workflows**

---

##  Multi-Agent Architecture

| Agent        | Responsibility                     |
| ------------ | ---------------------------------- |
|  Architect | Breaks goal into workflow steps    |
|  Auditor   | Validates compliance & correctness |
|  Executor   | Executes actions                   |
|  Sentinel  | Handles failures & retries         |
|  Historian | Stores memory & improves decisions |

---

## System Architecture

```text
User → React UI → FastAPI Backend → LangGraph Engine
                                   ↓
                             Multi-Agent System
                                   ↓
       ┌───────────────┬───────────────┬───────────────┐
       │ SQLite DB     │ Vector Store  │ Ollama LLM     │
       │ (Audit Logs)  │ (Memory)      │ (Local AI)     │
       └───────────────┴───────────────┴───────────────┘
```

---

##  Project Structure

```text
sentinelflow-ai/
│
├── backend/
│   ├── agents/
│   │   ├── architect_agent.py
│   │   ├── auditor_agent.py
│   │   ├── executor_agent.py
│   │   ├── sentinel_agent.py
│   │   └── historian_agent.py
│   │
│   ├── workflows/
│   │   └── workflow_engine.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   └── vector_store.py
│   │
│   └── main.py
│
├── frontend/
│   └── app/
│       ├── src/
│       │   ├── App.js
│       │   ├── WorkflowGraph.js
│       │   └── components/
│       │
│       └── package.json
│
├── requirements.txt
└── README.md

```
---

##  Technologies & Tools

###  Backend

* Python
* FastAPI
* LangChain + LangGraph

###  Frontend

* React.js
* JavaScript

###  AI & Intelligence

* Ollama (Local LLM)
* Llama3 (Open-source model)
* ChromaDB (Vector Store)

###  Database

* SQLite (workflow history & logs)

###  Development

* Cursor AI
* Git & GitHub

---

##  Key Features

* Multi-agent workflow orchestration
* Autonomous execution (90%+ without human intervention)
* Self-healing failure handling
* Real-time execution logs (audit trail)
* AI-generated tasks & insights
* Workflow history tracking
* Local AI (no paid APIs required)

---

##  System Requirements

### Minimum

* 8 GB RAM
* 10 GB free space

### Recommended

* 16 GB RAM
* Apple Silicon (M1/M2/M3) or equivalent

---

#  Setup & Installation

---

##  macOS

### Install dependencies

```bash
brew install python node git ollama
```

### Start Ollama

```bash
brew services start ollama
```

### Pull model

```bash
ollama pull llama3
```

---

##  Windows

Install:

* Python → https://www.python.org
* Node.js → https://nodejs.org
* Git → https://git-scm.com
* Ollama → https://ollama.com

Start Ollama:

```bash
ollama serve
```

Pull model:

```bash
ollama pull llama3
```

---

#  Run the Project

---

##  Backend

```bash
cd sentinelflow-ai
python -m venv venv
```

### Activate environment

**macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

---

### Install & run

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Backend: http://127.0.0.1:8000

---

##  Frontend

```bash
cd frontend/app
npm install
npm start
```

Frontend: http://localhost:3000

---

#  How to Use

1. Open the dashboard (localhost:3000)
2. Select a demo or enter your own workflow goal
3. Click **Run Workflow**
4. Observe:

   * Agent execution
   * Workflow results
   * Execution logs
   * AI-generated tasks
   * Confidence score

---

##  API Endpoints

| Endpoint    | Method | Description             |
| ----------- | ------ | ----------------------- |
| `/workflow` | POST   | Execute workflow        |
| `/history`  | GET    | Retrieve past workflows |

---

##  Example Use Cases

* Vendor Payment Processing
* Employee Onboarding
* Contract Review
* Loan Approval
* IT Access Provisioning

---

##  Impact Model

**Assumptions:**

* Manual workflow: 30 minutes
* AI workflow: 10 minutes
* 100 workflows/day

**Results:**

* Time saved: ~33 hours/day
* Cost savings: ~₹5.5 Lakhs/month
* Reduced SLA breaches

---

##  Key Advantages

* Fully local AI (data privacy safe)
* No paid APIs required
* Scalable architecture
* Enterprise-ready design

---

##  Why This Project Stands Out

* Multi-agent collaboration
* Autonomous decision-making
* Self-healing workflows
* Real-world enterprise applicability
* Full auditability + AI memory

---

##  Author

**Ravindra Suthar**

* GitHub: https://github.com/Ravindra8829
* LinkedIn: https://www.linkedin.com/in/ravindra-suthar/

---

##  Final Note

SentinelFlow AI is not just automation —
it is **Autonomous Enterprise Intelligence**.

---
