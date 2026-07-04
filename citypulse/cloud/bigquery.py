from google.cloud import bigquery

from citypulse.core.config import settings


class BigQueryClient:

    def __init__(self):

        self.client = bigquery.Client(
            project=settings.GCP_PROJECT_ID
        )

        self.dataset = settings.BIGQUERY_DATASET

    def test_connection(self):

        print("=" * 50)
        print("Connected to BigQuery")
        print(f"Project : {self.client.project}")
        print("=" * 50)

    def create_complaints_table(self):

        table_id = (
            f"{self.client.project}."
            f"{self.dataset}.complaints"
        )

        schema = [
            bigquery.SchemaField("report_id", "STRING"),
            bigquery.SchemaField("raw_text", "STRING"),
            bigquery.SchemaField("image_url", "STRING"),
            bigquery.SchemaField("latitude", "FLOAT"),
            bigquery.SchemaField("longitude", "FLOAT"),
            bigquery.SchemaField("ward", "STRING"),
            bigquery.SchemaField("created_at", "TIMESTAMP"),
        ]

        table = bigquery.Table(
            table_id,
            schema=schema,
        )

        table = self.client.create_table(
            table,
            exists_ok=True,
        )

        print(f"✅ Table ready : {table.table_id}")