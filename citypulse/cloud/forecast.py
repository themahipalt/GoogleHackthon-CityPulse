from citypulse.cloud.bigquery import BigQueryClient


class ForecastClient:

    def __init__(self):

        self.bigquery = BigQueryClient()

    def train_model(self):

        query = f"""
        CREATE OR REPLACE MODEL
        `{self.bigquery.client.project}.{self.bigquery.dataset}.complaint_forecast`

        OPTIONS(
            MODEL_TYPE='ARIMA_PLUS',
            TIME_SERIES_TIMESTAMP_COL='day',
            TIME_SERIES_DATA_COL='total_complaints'
        ) AS

        SELECT
            DATE(created_at) AS day,
            COUNT(*) AS total_complaints
        FROM
            `{self.bigquery.client.project}.{self.bigquery.dataset}.complaints`
        GROUP BY day
        ORDER BY day
        """

        self.bigquery.client.query(query).result()

        print("✅ Forecast model trained successfully.")