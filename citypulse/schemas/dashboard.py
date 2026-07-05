from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_complaints: int
    high_severity: int
    top_ward: str
    forecast: float