from datetime import datetime

from pydantic import BaseModel


class ComplaintReport(BaseModel):

    report_id: str

    raw_text: str

    image_url: str | None = None

    latitude: float

    longitude: float

    ward: str

    created_at: datetime | None = None