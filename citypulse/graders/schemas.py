from enum import Enum
from pydantic import BaseModel, Field


class ComplaintCategory(str, Enum):
    POTHOLE = "pothole"
    GARBAGE = "garbage"
    STREETLIGHT = "streetlight"
    TRAFFIC = "traffic"
    OTHER = "other"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ComplaintReport(BaseModel):
    """Raw citizen input — yeh tera 'Observation' hai"""
    report_id: str
    raw_text: str
    image_url: str | None = None
    latitude: float
    longitude: float
    ward: str


class TriageResult(BaseModel):
    """Model ka output — yeh tera 'Action' hai"""
    report_id: str
    category: ComplaintCategory
    severity: Severity
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


class TriageScore(BaseModel):
    """Grader ka output — yeh tera 'Reward' hai"""
    report_id: str
    score: float = Field(ge=0.0, le=1.0)
    category_correct: bool
    severity_correct: bool
    notes: str