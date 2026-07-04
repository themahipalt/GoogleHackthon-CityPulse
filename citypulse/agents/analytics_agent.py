from google import genai

from citypulse.core.config import settings
from citypulse.cloud.bigquery import BigQueryClient
from citypulse.schemas.analytics import AnalyticsResponse
from citypulse.schemas.analytics import AnalyticsResponse

class AnalyticsAgent:

    def __init__(self):
        
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )
        self.bigquery = BigQueryClient()

    async def generate_sql(self, question: str) -> str:

        prompt = f"""
You are an expert BigQuery SQL generator.

Project ID:
{settings.GCP_PROJECT_ID}

Dataset:
{settings.BIGQUERY_DATASET}

Table:
complaints

Schema:

report_id STRING
raw_text STRING
image_url STRING
latitude FLOAT
longitude FLOAT
ward STRING
created_at TIMESTAMP

Rules:

1. Return ONLY SQL.
2. No explanation.
3. No markdown.
4. Use Standard SQL.
5. Always use the fully qualified table name.

Question:

{question}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()
    

    async def ask(self, question: str):

        sql = await self.generate_sql(question)

        print("\nGenerated SQL\n")
        print(sql)

        rows = self.bigquery.execute_query(sql)

        explanation = await self.explain_result(
            question,
            sql,
            rows,
        )

        return AnalyticsResponse(
                question=question,
                sql=sql,
                rows=rows,
                answer=explanation,
                )
    


    
    async def explain_result(
    self,
    question: str,
    sql: str,
    rows: list[dict]
) -> str:

        prompt = f"""
    You are an AI Decision Intelligence assistant for a Smart City platform.

    The user asked:

    {question}

    The SQL executed was:

    {sql}

    The query returned:

    {rows}

    Write a concise answer for a city official.

    Rules:
    - Do not mention SQL.
    - Do not mention databases.
    - Keep the answer under 80 words.
    - Mention important numbers.
    - Give one actionable recommendation if appropriate.
    """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()