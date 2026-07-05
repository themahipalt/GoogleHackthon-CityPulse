from google.cloud import bigquery


class DashboardRepository:

    def __init__(self):

        self.client = bigquery.Client()

        self.complaints_table = (
            "linear-quasar-497618-a9.citypulse.complaints"
        )

        self.triage_table = (
            "linear-quasar-497618-a9.citypulse.triage_results"
        )

    # -----------------------------------------
    # Total Complaints
    # -----------------------------------------

    def get_total_complaints(self):

        sql = f"""
        SELECT COUNT(*) AS total
        FROM `{self.complaints_table}`
        """

        return list(self.client.query(sql))[0].total

    # -----------------------------------------
    # High Severity Complaints
    # -----------------------------------------

    def get_high_severity(self):

        sql = f"""
        SELECT COUNT(*) AS total
        FROM `{self.triage_table}`
        WHERE LOWER(severity) = 'high'
        """

        return list(self.client.query(sql))[0].total

    # -----------------------------------------
    # Ward with Maximum Complaints
    # -----------------------------------------

    def get_top_ward(self):

        sql = f"""
        SELECT ward
        FROM `{self.complaints_table}`
        GROUP BY ward
        ORDER BY COUNT(*) DESC
        LIMIT 1
        """

        rows = list(self.client.query(sql))

        if rows:
            return rows[0].ward

        return "-"

    # -----------------------------------------
    # Forecast
    # -----------------------------------------

    def get_forecast(self):

        sql = """
        SELECT forecast_value
        FROM ML.FORECAST(
            MODEL `linear-quasar-497618-a9.citypulse.complaint_forecast`,
            STRUCT(7 AS horizon)
        )
        LIMIT 1
        """

        try:

            rows = list(self.client.query(sql))

            if rows:
                return round(rows[0].forecast_value, 2)

            return 0

        except Exception:

            # Forecast model not created yet
            return 0