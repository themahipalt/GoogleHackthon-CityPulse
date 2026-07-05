from pydantic import BaseModel


class RecommendationResult(BaseModel):

    summary: str

    recommendation: str

    confidence: float