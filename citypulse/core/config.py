import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    def __init__(self):

        # Gemini
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

        # Google Cloud
        self.GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
        self.BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")


settings = Settings()