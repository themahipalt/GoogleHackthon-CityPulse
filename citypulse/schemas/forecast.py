from datetime import datetime

from pydantic import BaseModel


class ForecastResult(BaseModel):

    forecast_timestamp: datetime

    predicted_complaints: float

    lower_bound: float

    upper_bound: float

    confidence_level: float