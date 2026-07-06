# 🏙️ CityPulse

> **AI-Powered Citizen Complaint Intelligence Platform for Smart Cities**

🏆 Google Cloud Gen AI Hackathon 2026

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-green)
![Angular](https://img.shields.io/badge/Angular-red)
![Google ADK](https://img.shields.io/badge/Google-ADK-blue)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange)
![BigQuery](https://img.shields.io/badge/BigQuery-Google-blue)
![Cloud Run](https://img.shields.io/badge/Cloud-Run-success)

---

# 🚀 Overview

CityPulse is an AI-powered platform that helps city authorities manage citizen complaints more efficiently.

Instead of manually reviewing complaints, CityPulse uses **Google ADK** and **Gemini** to:

- 🤖 Understand complaints
- 🏷️ Classify complaint category
- 🚨 Detect severity
- 💡 Generate AI recommendations
- 📊 Visualize complaint trends
- ☁️ Store analytics in BigQuery

---

# ✨ Features

- AI Complaint Triage
- Severity Detection
- Dashboard Analytics
- Complaint Trend Visualization
- BigQuery Integration
- AI Recommendation Engine
- REST APIs with FastAPI
- Angular Dashboard
- Cloud Run Deployment
- Google ADK Multi-Agent Workflow

---

# 🏗️ Architecture

```text
Citizen
    │
    ▼
Angular Dashboard
    │
    ▼
FastAPI Backend
    │
    ▼
Google ADK Root Agent
    │
 ┌──┴───────────────┐
 │                  │
 ▼                  ▼
Gemini         BigQuery
 │                  │
 └──────────┬───────┘
            ▼
 Dashboard & AI Insights
```

---

# 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | Angular 20 |
| Backend | FastAPI |
| AI | Google ADK + Gemini 2.5 Flash |
| Database | BigQuery, SQLite |
| Cloud | Google Cloud Run |
| Charts | Chart.js |
| Language | Python |

---

# 📂 Project Structure

```text
citypulse/
├── agents/
├── api/
├── cloud/
├── database/
├── schemas/
├── services/
├── orchestrator/
├── tests/
├── data/
└── main.py
```

---

# 🚀 Getting Started

## Backend

```bash
uv sync
uv run uvicorn citypulse.main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd citypulse-ui
npm install
ng serve
```

Frontend:

```
http://localhost:4200
```

---

## Google ADK Web

```bash
uv run adk web
```

---

# 📸 Demo

### Dashboard

- Complaint Statistics
- Trend Analysis
- Forecast
- AI Recommendations

### APIs

- `POST /triage`
- `POST /chat`
- `GET /dashboard`
- `GET /dashboard/trend`

### AI Workflow

Citizen Complaint

↓

Google ADK Agent

↓

Gemini Analysis

↓

BigQuery

↓

Dashboard Insights

---

# 🌟 Why CityPulse?

✅ AI-powered complaint understanding

✅ Multi-agent architecture using Google ADK

✅ Explainable recommendations

✅ Real-time analytics dashboard

✅ Cloud-native deployment

✅ Scalable for smart cities

---

# 🔮 Future Enhancements

- Image-based complaint analysis
- Voice complaint support
- Predictive analytics
- GIS-based complaint maps
- Automated work order generation

---

# 👨‍💻 Author

**Mahipal Thakur**

Software Engineer | Google Cloud Gen AI Hackathon 2026

Built with ❤️ using **Google ADK**, **Gemini**, **BigQuery**, **FastAPI**, **Angular**, and **Google Cloud Run**.