from citypulse.cloud.bigquery import BigQueryClient
from citypulse.database.repository import ComplaintRepository
from citypulse.schemas.complaint import ComplaintReport


class BigQueryUploader:

    def __init__(self):

        self.repository = ComplaintRepository()
        self.bigquery = BigQueryClient()

    def upload_complaints(self):

        complaints = self.repository.get_all_complaints()

        table_id = (
            f"{self.bigquery.client.project}."
            f"{self.bigquery.dataset}.complaints"
        )

        rows = []

        for complaint in complaints:

            rows.append(
                {
                    "report_id": complaint.report_id,
                    "raw_text": complaint.raw_text,
                    "image_url": complaint.image_url,
                    "latitude": complaint.latitude,
                    "longitude": complaint.longitude,
                    "ward": complaint.ward,
                    "created_at": None,
                }
            )

        errors = self.bigquery.client.insert_rows_json(
            table_id,
            rows,
        )

        if errors:
            print("❌ Upload Failed")
            print(errors)
        else:
            print(f"✅ Uploaded {len(rows)} complaints")