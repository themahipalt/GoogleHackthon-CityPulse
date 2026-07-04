from pydantic import BaseModel


class AnalyticsResponse(BaseModel):

    question: str

    sql: str

    rows: list[dict]

    answer: str