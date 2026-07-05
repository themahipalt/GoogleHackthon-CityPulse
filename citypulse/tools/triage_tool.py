from citypulse.schemas.complaint import ComplaintReport
from citypulse.services.triage_service import TriageService

service = TriageService()


async def triage_tool(complaint: str) -> str:
    """
    Classify a citizen complaint.
    """

    report = ComplaintReport(
        report_id="TEMP",
        raw_text=complaint,
        image_url=None,
        latitude=0.0,
        longitude=0.0,
        ward="Unknown",
    )

    result = await service.triage(report)

    return result.model_dump_json(indent=2)