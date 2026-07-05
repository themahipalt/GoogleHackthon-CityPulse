from datetime import datetime

from citypulse.database.connection import get_connection
from citypulse.schemas.complaint import ComplaintReport
from citypulse.graders.schemas import TriageResult


class ComplaintRepository:

    def save_complaint(
        self,
        complaint: ComplaintReport,
        created_at: datetime | None = None,
    ):
        conn = get_connection()
        cursor = conn.cursor()

        # Use provided timestamp or fallback to current time
        timestamp = (
            created_at.strftime("%Y-%m-%d %H:%M:%S")
            if created_at
            else None
        )

        cursor.execute(
            """
            INSERT INTO complaints (
                report_id,
                raw_text,
                image_url,
                latitude,
                longitude,
                ward,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, COALESCE(?, datetime('now')))
            """,
            (
                complaint.report_id,
                complaint.raw_text,
                complaint.image_url,
                complaint.latitude,
                complaint.longitude,
                complaint.ward,
                timestamp,
            ),
        )

        conn.commit()
        conn.close()

    def save_triage_result(self, result: TriageResult):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO triage_results (
                report_id,
                category,
                severity,
                confidence,
                rationale,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, datetime('now'))
            """,
            (
                result.report_id,
                result.category.value,
                result.severity.value,
                result.confidence,
                result.rationale,
            ),
        )

        conn.commit()
        conn.close()

    def get_complaint(self, report_id: str):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM complaints
            WHERE report_id = ?
            """,
            (report_id,),
        )

        row = cursor.fetchone()

        conn.close()

        return row

    def get_all_complaints(self) -> list[ComplaintReport]:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                report_id,
                raw_text,
                image_url,
                latitude,
                longitude,
                ward,
                created_at
            FROM complaints
            """
        )

        rows = cursor.fetchall()

        connection.close()

        complaints = []

        for row in rows:

            complaints.append(
                ComplaintReport(
                    report_id=row["report_id"],
                    raw_text=row["raw_text"],
                    image_url=row["image_url"],
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                    ward=row["ward"],
                    created_at=row["created_at"],
                )
            )

        return complaints