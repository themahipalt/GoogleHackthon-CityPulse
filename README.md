# 🏙️ CityPulse
### AI-Powered Decision Intelligence Platform for Smart Cities

> 🏆 Google Cloud Gen AI Hackathon 2026 Submission

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Google Cloud](https://img.shields.io/badge/Google-Cloud-blue)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange)
![Vertex AI](https://img.shields.io/badge/Vertex-AI-purple)
![ADK](https://img.shields.io/badge/Google-ADK-red)
![Status](https://img.shields.io/badge/Phase-1%20Completed-success)

---

# 📖 Overview

CityPulse is an AI-powered Decision Intelligence Platform built on Google Cloud that transforms citizen complaints into actionable insights for city administrators.

Instead of simply storing complaints, CityPulse:

- 🧠 Understands complaints using Gemini
- 🤖 Uses AI agents to automate decision making
- 📊 Detects patterns and anomalies
- 📈 Predicts future issues
- 💡 Generates explainable recommendations
- 📉 Visualizes insights through dashboards

Our vision is to help governments move from **reactive governance** to **proactive, AI-driven decision making.**

---

# 🎯 Problem Statement

Modern cities generate massive amounts of structured and unstructured data through:

- Citizen complaints
- Public transportation
- Waste management
- Utilities
- Environmental monitoring
- Public safety
- Healthcare
- Social services

Unfortunately, this data often remains siloed and difficult to analyze.

CityPulse converts raw data into intelligent recommendations using Google Cloud AI.

---

# 🏗️ System Architecture

```text
                         Citizen Complaint
                                │
                                ▼
                  Gemini 2.5 Flash (LLM)
               Understands Natural Language
                                │
                                ▼
                   ADK Orchestrator Agent
                                │
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
       ▼                        ▼                        ▼
 Triage Agent          BigQuery Analytics         Vertex AI RAG
       │                        │                        │
       └────────────────────────┼────────────────────────┘
                                │
                                ▼
                 Forecast & Anomaly Detection
                                │
                                ▼
              Recommendation & Explainability
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
        ┌─────────────────┼────────────────┐
        │                 │                │
        ▼                 ▼                ▼
   Gemini API        Vertex AI         Cloud Functions
        │                 │                │
        └─────────────────┼────────────────┘
                          │
                          ▼
                      BigQuery
                          │
          ┌───────────────┼───────────────┐
          │                               │
          ▼                               ▼
      AlloyDB                     Cloud Storage
          │
          ▼
     Looker Studio
```

---

# 🤖 Multi-Agent Architecture

```text
                ADK Orchestrator
                      │
 ┌────────────┬─────────────┬─────────────┐
 │            │             │             │
 ▼            ▼             ▼             ▼
Triage     Query        Forecast    Recommendation
Agent      Agent         Agent          Agent
 │            │             │             │
 └────────────┴─────────────┴─────────────┘
                      │
                      ▼
               Explainability Agent
```

---

# 🚀 Features

### ✅ Current

- Gemini Complaint Understanding
- AI Complaint Classification
- Severity Detection
- Explainable Response
- FastAPI REST API
- Swagger Documentation

---

### 🚧 Upcoming

- SQLite Storage
- BigQuery Analytics
- RAG Knowledge Search
- Multi-Agent Workflow
- Forecasting
- Recommendation Engine
- Explainability Agent
- Dashboard
- Cloud Deployment

---

# 🛠️ Technology Stack

| Layer | Technology |
|---------|------------|
| Backend | FastAPI |
| AI Model | Gemini 2.5 Flash |
| AI Platform | Vertex AI |
| Multi-Agent | Google ADK |
| Analytics | BigQuery |
| Database | AlloyDB |
| Local Development | SQLite |
| RAG | Vertex AI RAG |
| Storage | Cloud Storage |
| Dashboard | Looker Studio |
| Deployment | Cloud Run |
| Automation | Cloud Functions |
| Monitoring | Cloud Logging |

---

# 📂 Project Structure

```text
citypulse/

├── api/
├── agents/
├── core/
├── database/
├── graders/
├── tests/
├── data/
├── README.md
└── pyproject.toml
```

---

# 📍 Current Progress

| Phase | Status |
|--------|--------|
| Project Setup | ✅ |
| Gemini Integration | ✅ |
| Complaint Triage Agent | ✅ |
| FastAPI Backend | ✅ |
| Swagger API | ✅ |

---

# 🛣️ Development Roadmap

## ✅ Phase 0
Project Setup

## ✅ Phase 1
Gemini Complaint Triage

## ⏳ Phase 2
Database Layer (SQLite → AlloyDB)

## ⏳ Phase 3
Synthetic Dataset Generation

## ⏳ Phase 4
Natural Language Query Engine

## ⏳ Phase 5
Anomaly Detection

## ⏳ Phase 6
Forecasting

## ⏳ Phase 7
Recommendation & Explainability

## ⏳ Phase 8
Dashboard & Google Cloud Deployment

---

# 🎯 Future Vision

CityPulse is designed to become an AI-powered Decision Intelligence Platform that helps governments and organizations:

- Predict city-wide issues before they occur.
- Allocate resources intelligently.
- Improve citizen satisfaction.
- Enable explainable AI-driven governance.
- Build smarter, more resilient communities.

---

# 👨‍💻 Author

**Mahipal Thakur**

Google Cloud Gen AI Hackathon 2026