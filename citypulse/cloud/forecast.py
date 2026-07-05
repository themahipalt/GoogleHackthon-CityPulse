from citypulse.cloud.bigquery import BigQueryClient
from citypulse.schemas.forecast import ForecastResult


class ForecastClient:

    def __init__(self):

        self.bigquery = BigQueryClient()

    def get_forecast(
        self,
        horizon: int = 7,
    ) -> list[ForecastResult]:

        query = f"""
        SELECT
            forecast_timestamp,
            forecast_value,
            prediction_interval_lower_bound,
            prediction_interval_upper_bound,
            confidence_level
        FROM ML.FORECAST(
            MODEL `{self.bigquery.client.project}.{self.bigquery.dataset}.complaint_forecast`,
            STRUCT({horizon} AS horizon)
        )
        """

        rows = self.bigquery.client.query(query).result()

        forecasts = []

        for row in rows:

            forecasts.append(
                ForecastResult(
                    forecast_timestamp=row["forecast_timestamp"],
                    predicted_complaints=row["forecast_value"],
                    lower_bound=row["prediction_interval_lower_bound"],
                    upper_bound=row["prediction_interval_upper_bound"],
                    confidence_level=row["confidence_level"],
                )
            )

        return forecasts