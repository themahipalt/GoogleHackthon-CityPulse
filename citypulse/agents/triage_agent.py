import json

from google import genai

from citypulse.core.config import settings
from citypulse.graders.schemas import ComplaintReport, TriageResult

client = genai.Client(api_key=settings.GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are a civic complaint triage agent.

Respond ONLY with valid JSON.

{
    "category":"pothole|garbage|streetlight|traffic|other",
    "severity":"low|medium|high",
    "confidence":0.95,
    "rationale":"one sentence"
}
"""


async def triage_report(report: ComplaintReport) -> TriageResult:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
{SYSTEM_PROMPT}

Complaint:
{report.raw_text}
"""
    )

    print("========== GEMINI RESPONSE ==========")
    print(response.text)
    print("=====================================")

    clean_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    print("========== CLEANED RESPONSE ==========")
    print(clean_text)
    print("======================================")

    data = json.loads(clean_text)

    return TriageResult(
        report_id=report.report_id,
        **data
    )