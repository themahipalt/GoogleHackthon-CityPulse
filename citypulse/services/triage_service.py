from citypulse.agents.triage_agent import triage_report
from citypulse.schemas.complaint import ComplaintReport


class TriageService:

    async def triage(self, report: ComplaintReport):
        return await triage_report(report)