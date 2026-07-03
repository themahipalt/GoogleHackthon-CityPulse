from fastapi import FastAPI

from citypulse.database.repository import ComplaintRepository
from citypulse.graders.schemas import ComplaintReport
from citypulse.agents.triage_agent import triage_report

app = FastAPI()

repository = ComplaintRepository()


@app.post("/triage")
async def triage(report: ComplaintReport):

    # Save original complaint
    repository.save_complaint(report)

    # Gemini classification
    result = await triage_report(report)

    # Save Gemini prediction
    repository.save_triage_result(result)

    return result