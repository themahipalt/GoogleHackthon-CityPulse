from google import genai

from citypulse.core.config import settings
from citypulse.cloud.forecast import ForecastClient
from citypulse.agents.analytics_agent import AnalyticsAgent
from citypulse.schemas.recommendation import RecommendationResult


class RecommendationAgent:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.forecast = ForecastClient()

        self.analytics = AnalyticsAgent()

    async def recommend(self) -> RecommendationResult:

        forecast = self.forecast.get_forecast()

        analytics = await self.analytics.ask(
            "Which ward has the highest complaints?"
        )

        forecast_text = "\n".join(
            [
                f"{day.forecast_timestamp.date()} : {day.predicted_complaints:.2f}"
                for day in forecast
            ]
        )

        prompt = f"""
    You are an urban planning AI.

    Forecast:

    {forecast_text}

    Highest Complaint Ward:

    {analytics.answer}

    Return ONLY JSON.

    Schema

    {{
        "summary":"",
        "recommendation":"",
        "confidence":0.95
    }}
    """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        import json
        print("\n========== GEMINI RESPONSE ==========")
        print(response.text)
        print("=====================================\n")
        import json

        text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        print(text)

        data = json.loads(text)

        return RecommendationResult(**data)