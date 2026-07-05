# 🏙️ CityPulse

# AI-Powered Decision Intelligence Platform for Smart Cities

Start : uv run uvicorn citypulse.main:app --reload
> 🏆 Google Cloud Gen AI Hackathon 2026 Submission

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange)
![BigQuery](https://img.shields.io/badge/Google-BigQuery-blue)
![Google Cloud](https://img.shields.io/badge/Google-Cloud-success)
![Status](https://img.shields.io/badge/Phase-5%20Completed-success)

---

# 📖 Overview

CityPulse is an AI-powered Decision Intelligence Platform that helps city administrations transform citizen complaints into actionable insights using Google Cloud AI.

Instead of simply storing complaints, CityPulse:

- 🤖 Understands complaints using Gemini 2.5 Flash
- 🏷️ Automatically classifies complaints
- 🚨 Detects severity
- 💾 Stores complaints locally in SQLite
- ☁️ Synchronizes data with Google BigQuery
- 📊 Answers natural language analytics questions
- 🧠 Generates AI-powered recommendations

Our vision is to move governments from **reactive governance** to **proactive AI-assisted decision making**.

---

# 🎯 Problem Statement

Cities receive thousands of complaints every day through different channels.

Unfortunately:

- Complaints remain siloed.
- Decision makers must manually analyze data.
- Trends are difficult to identify.
- Resource allocation is reactive instead of proactive.

CityPulse leverages Gemini and Google Cloud to automatically understand complaints, analyze city-wide trends, and assist officials with intelligent recommendations.

---

# 🚀 Current Features

## ✅ Implemented

- 🤖 Gemini Complaint Triage
- 🏷️ Complaint Category Classification
- 🚨 Severity Detection
- 📦 SQLite Repository Pattern
- 🧪 Synthetic Dataset Generator (Gemini)
- ☁️ Google BigQuery Integration
- 📊 AI Analytics Agent
- 💬 Natural Language → SQL Generation
- 📈 BigQuery Query Execution
- 🧠 AI-generated Decision Intelligence
- ⚡ FastAPI REST API
- 📖 Swagger API Documentation

---

## 🚧 Coming Soon

- 📈 Forecasting Agent
- 🚨 Anomaly Detection
- 💡 Recommendation Agent
- 🤖 Google ADK Multi-Agent Orchestrator
- 🔍 RAG Knowledge Search
- 📊 Looker Studio Dashboard
- ☁️ Cloud Run Deployment

---

# 🏗️ Current Architecture

```text
                    Citizen Complaint
                           │
                           ▼
                 Gemini 2.5 Flash
                           │
                           ▼
                    Triage Agent
                           │
                           ▼
                  SQLite Repository
                           │
                           ▼
                 BigQuery Uploader
                           │
                           ▼
                  Google BigQuery
                           │
                           ▼
                  Analytics Agent
                           │
                           ▼
            AI Insights & Recommendations
```

---

# 🔮 Target Architecture

```text
                         Citizen Complaint
                                │
                                ▼
                  Gemini 2.5 Flash (LLM)
                                │
                                ▼
                   ADK Orchestrator Agent
                                │
      ┌─────────────────────────┼────────────────────────┐
      │                         │                        │
      ▼                         ▼                        ▼
 Triage Agent          Analytics Agent          Forecast Agent
      │                         │                        │
      └─────────────────────────┼────────────────────────┘
                                │
                                ▼
                 Recommendation Agent
                                │
                                ▼
                Explainability Agent
                                │
                                ▼
                  Looker Studio Dashboard
                                │
                                ▼
          Citizens • Officials • Decision Makers
```

---

# ☁️ Google Cloud Architecture

```text
                    FastAPI Backend
                           │
                           ▼
                       Cloud Run
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   Gemini API        Google BigQuery      Vertex AI
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                    Looker Studio
```

---

# 🤖 AI Agent Workflow

```text
User Question

        │

        ▼

Analytics Agent

        │

        ▼

Gemini 2.5 Flash

        │

        ▼

BigQuery SQL

        │

        ▼

Google BigQuery

        │

        ▼

Query Result

        │

        ▼

Gemini Explanation

        │

        ▼

Decision Intelligence
```

---

# 🛠️ Technology Stack

| Layer | Technology |
|---------|------------|
| Backend | FastAPI |
| Language | Python 3.14 |
| AI Model | Gemini 2.5 Flash |
| Cloud Analytics | BigQuery |
| Local Database | SQLite |
| Google Cloud | Cloud SDK |
| Data Validation | Pydantic |
| API Testing | Swagger UI |
| Testing | Pytest |
| Future Orchestration | Google ADK |
| Future Dashboard | Looker Studio |

---

# 📂 Project Structure

```text
citypulse/

├── agents/
│   ├── analytics_agent.py
│   ├── generator_agent.py
│   └── triage_agent.py
│
├── api/
│
├── cloud/
│   ├── bigquery.py
│   └── uploader.py
│
├── core/
│
├── database/
│
├── graders/
│
├── schemas/
│
├── scripts/
│
├── tests/
│
├── data/
│
├── README.md
└── pyproject.toml
```

---

# 📍 Current Progress

| Phase | Status |
|---------|--------|
| ✅ Project Setup | Complete |
| ✅ Gemini Integration | Complete |
| ✅ Complaint Triage Agent | Complete |
| ✅ SQLite Repository | Complete |
| ✅ Synthetic Dataset Generation | Complete |
| ✅ Google BigQuery Integration | Complete |
| ✅ Analytics Agent | Complete |
| 🚧 Forecast Agent | In Progress |

---

# 🛣️ Development Roadmap

## ✅ Phase 0

Project Setup

## ✅ Phase 1

Gemini Complaint Triage

## ✅ Phase 2

SQLite Repository Layer

## ✅ Phase 3

Synthetic Dataset Generation

## ✅ Phase 4

Google BigQuery Integration

## ✅ Phase 5

Analytics Agent

## 🚧 Phase 6

Forecasting Agent

## ⏳ Phase 7

Recommendation Agent

## ⏳ Phase 8

Google ADK Multi-Agent Orchestrator

## ⏳ Phase 9

Looker Studio Dashboard

## ⏳ Phase 10

Cloud Run Deployment

---

# 🎯 Example Analytics

### User

```
Which ward has the highest complaints?
```

### Generated SQL

```sql
SELECT
    ward,
    COUNT(*) AS total_complaints
FROM
    `project.citypulse.complaints`
GROUP BY ward
ORDER BY total_complaints DESC
LIMIT 1;
```

### AI Response

```
Ward 5 currently has the highest number of complaints.

Recommendation:
Investigate the complaint categories in Ward 5 and prioritize municipal resources.
```

---

# 🎯 Vision

CityPulse aims to become an AI-powered Decision Intelligence Platform that enables governments to:

- Predict city-wide issues before they occur.
- Detect anomalies automatically.
- Optimize municipal resource allocation.
- Provide explainable AI recommendations.
- Improve citizen satisfaction.
- Build smarter and more resilient cities.

---

# 👨‍💻 Author

**Mahipal Thakur**

Software Engineer | Google Cloud Gen AI Hackathon 2026

Built using **Google Cloud**, **Gemini 2.5 Flash**, **BigQuery**, **FastAPI**, and **Python**.