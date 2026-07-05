from datetime import UTC, datetime

from google.cloud import bigquery

from citypulse.core.config import settings


class BigQueryClient:

    def __init__(self):

        self.client = bigquery.Client(
            project=settings.GCP_PROJECT_ID
        )

        self.dataset = settings.BIGQUERY_DATASET

    # ---------------------------------------------
    # Connection
    # ---------------------------------------------

    def test_connection(self):

        print("=" * 60)
        print("✅ Connected to BigQuery")
        print(f"Project : {self.client.project}")
        print("=" * 60)

    # ---------------------------------------------
    # Create Complaints Table
    # ---------------------------------------------

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

        self.client.create_table(
            table,
            exists_ok=True,
        )

        print("✅ Complaints table ready")

    # ---------------------------------------------
    # Create Triage Results Table
    # ---------------------------------------------

    def create_triage_table(self):

        table_id = (
            f"{self.client.project}."
            f"{self.dataset}.triage_results"
        )

        schema = [
            bigquery.SchemaField("report_id", "STRING"),
            bigquery.SchemaField("category", "STRING"),
            bigquery.SchemaField("severity", "STRING"),
            bigquery.SchemaField("confidence", "FLOAT"),
            bigquery.SchemaField("rationale", "STRING"),
            bigquery.SchemaField("processed_at", "TIMESTAMP"),
        ]

        table = bigquery.Table(
            table_id,
            schema=schema,
        )

        self.client.create_table(
            table,
            exists_ok=True,
        )

        print("✅ Triage Results table ready")

    # ---------------------------------------------
    # Insert Complaint
    # ---------------------------------------------

    def insert_complaint(self, report):

        table_id = (
            f"{self.client.project}."
            f"{self.dataset}.complaints"
        )

        rows = [
            {
                "report_id": report.report_id,
                "raw_text": report.raw_text,
                "image_url": getattr(report, "image_url", None),
                "latitude": getattr(report, "latitude", None),
                "longitude": getattr(report, "longitude", None),
                "ward": getattr(report, "ward", None),
                "created_at": datetime.now(UTC).isoformat(),
            }
        ]

        errors = self.client.insert_rows_json(
            table_id,
            rows,
        )

        if errors:
            print("❌ Complaint insert failed")
            print(errors)
        else:
            print("✅ Complaint inserted into BigQuery")

    # ---------------------------------------------
    # Insert Triage Result
    # ---------------------------------------------

    def insert_triage_result(self, result):

        table_id = (
            f"{self.client.project}."
            f"{self.dataset}.triage_results"
        )

        rows = [
            {
                "report_id": result.report_id,
                "category": result.category,
                "severity": result.severity,
                "confidence": result.confidence,
                "rationale": result.rationale,
                "processed_at": datetime.now(UTC).isoformat(),
            }
        ]

        errors = self.client.insert_rows_json(
            table_id,
            rows,
        )

        if errors:
            print("❌ Triage insert failed")
            print(errors)
        else:
            print("✅ Triage Result inserted into BigQuery")

    # ---------------------------------------------
    # Execute Query
    # ---------------------------------------------

    def execute_query(self, query: str):

        query_job = self.client.query(query)

        results = query_job.result()

        rows = []

        for row in results:
            rows.append(dict(row))

        return rows