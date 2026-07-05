# 🎨 CityPulse UI

> **Angular 21 Frontend for the CityPulse AI-Powered Decision Intelligence Platform**

![Angular](https://img.shields.io/badge/Angular-21-red)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue)
![Angular Material](https://img.shields.io/badge/Angular-Material-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

---

# 📖 Overview

CityPulse UI is the modern Angular frontend for the **CityPulse** platform.

It provides an intuitive dashboard for city administrators to:

- 📊 Monitor complaint analytics
- 📈 View complaint forecasts
- 💡 Receive AI-generated recommendations
- 🤖 Interact with an AI Assistant
- 📍 Track complaint trends across city wards

The frontend communicates with the **FastAPI backend** and **Google ADK AI Orchestrator** to provide real-time decision intelligence.

---

# 🚀 Features

## ✅ Current

- Angular 21
- Standalone Components
- Angular Material
- Component-Based Architecture
- Lazy Loaded Routes
- Responsive Layout

---

## 🚧 Upcoming

- Dashboard
- Analytics Charts
- Forecast Visualization
- AI Chat
- Recommendation Panel
- Complaint Management
- Dark Mode
- Authentication
- Mobile Responsive UI

---

# 🏗️ Architecture

```text
                     Angular 21

                            │

                            ▼

                  Component-Based UI

                            │

        ┌───────────────────┼───────────────────┐

        ▼                   ▼                   ▼

   Dashboard           Analytics            AI Chat

        │                   │                   │

        └───────────────────┼───────────────────┘

                            ▼

                    Angular Services

                            │

                            ▼

                      FastAPI Backend

                            │

                            ▼

                    Google ADK Agents

                            │

                            ▼

       Gemini • BigQuery • BigQuery ML
```

---

# 📂 Project Structure

```text
src/

app/

├── core/
│   ├── guards/
│   ├── models/
│   └── services/
│
├── layout/
│   ├── navbar/
│   ├── sidebar/
│   └── shell/
│
├── shared/
│   ├── components/
│   └── pipes/
│
├── features/
│   ├── dashboard/
│   ├── analytics/
│   ├── forecast/
│   ├── recommendations/
│   ├── complaints/
│   └── chat/
│
├── app.config.ts
├── app.routes.ts
└── app.ts
```

---

# 🎨 Planned Dashboard

```text
+-------------------------------------------------------------+
| CityPulse                                   👤 Administrator |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
| 📊 Total Complaints | 🚨 High Severity | 📍 Top Ward         |
+-------------------------------------------------------------+

+---------------------------+---------------------------------+
| Complaint Trend           | Complaint Categories            |
+---------------------------+---------------------------------+

+-------------------------------------------------------------+
| 💡 AI Recommendation                                      |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
| 🤖 AI Assistant                                           |
+-------------------------------------------------------------+
```

---

# 🔌 Backend Integration

The frontend communicates with the CityPulse backend through REST APIs.

| Endpoint | Purpose |
|----------|---------|
| POST `/chat` | AI Assistant |
| POST `/triage` | Complaint Classification |
| GET `/analytics` | Complaint Analytics *(Upcoming)* |
| GET `/forecast` | Forecast Data *(Upcoming)* |
| GET `/recommendation` | AI Recommendation *(Upcoming)* |

---

# 🛠️ Technology Stack

| Layer | Technology |
|--------|------------|
| Framework | Angular 21 |
| Language | TypeScript |
| UI | Angular Material |
| Styling | SCSS |
| Routing | Angular Router |
| HTTP | HttpClient |
| Charts | ApexCharts *(Planned)* |
| State Management | Angular Signals |
| Icons | Angular Material Icons |

---

# 🚀 Getting Started

## Install Dependencies

```bash
npm install
```

---

## Run Development Server

```bash
ng serve
```

The application will be available at:

```
http://localhost:4200
```

---

## Build for Production

```bash
ng build
```

---

## Run Tests

```bash
ng test
```

---

# 🎯 Development Roadmap

- Responsive Dashboard
- Analytics Page
- Forecast Page
- Recommendation Page
- AI Chat Interface
- Charts & Visualizations
- Dark Theme
- Authenticationng g c layout/shell --standalone --skip-tests
- Cloud Deployment

---

# 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

Please open an issue or submit a pull request.

---

# 👨‍💻 Author

**Mahipal Thakur**

Software Engineer

Google Cloud Gen AI Hackathon 2026

---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.