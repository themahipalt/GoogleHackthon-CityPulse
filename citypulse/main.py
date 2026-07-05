from fastapi import FastAPI

from citypulse.api.chat import router as chat_router
from citypulse.agents.triage_agent import triage_report
from citypulse.database.repository import ComplaintRepository
from citypulse.schemas.complaint import ComplaintReport

app = FastAPI(
    title="CityPulse API",
    version="1.0.0",
)

repository = ComplaintRepository()


@app.post("/triage")
async def triage(report: ComplaintReport):

    # Save citizen complaint
    repository.save_complaint(report)

    # AI triage
    result = await triage_report(report)

    # Save AI prediction
    repository.save_triage_result(result)

    return result


# AI Chat API
app.include_router(chat_router)