from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from citypulse.api.chat import router as chat_router
from citypulse.api.dashboard import router as dashboard_router

from citypulse.agents.triage_agent import triage_report
from citypulse.cloud.bigquery import BigQueryClient
from citypulse.database.repository import ComplaintRepository
from citypulse.schemas.complaint import ComplaintReport

app = FastAPI(
    title="CityPulse API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

repository = ComplaintRepository()
bigquery = BigQueryClient()


@app.post("/triage")
async def triage(report: ComplaintReport):

    # Save complaint in SQLite
    repository.save_complaint(report)

    # AI Triaging
    result = await triage_report(report)

    # Save AI result in SQLite
    repository.save_triage_result(result)

    # Save complaint in BigQuery
    bigquery.insert_complaint(report)

    # Save AI result in BigQuery
    bigquery.insert_triage_result(result)

    return result


# APIs
app.include_router(chat_router)
app.include_router(dashboard_router)