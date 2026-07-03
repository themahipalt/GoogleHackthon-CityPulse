from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from citypulse.graders.schemas import ComplaintReport, TriageResult
from citypulse.agents.triage_agent import triage_report

app = FastAPI(title="CityPulse")


@app.post("/triage", response_model=TriageResult)
async def triage(report: ComplaintReport) -> TriageResult:
    return await triage_report(report)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}