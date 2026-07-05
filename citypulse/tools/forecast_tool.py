from citypulse.cloud.forecast import ForecastClient

forecast = ForecastClient()


def forecast_tool() -> str:
    """
    Returns the next 7-day complaint forecast.
    """

    result = forecast.get_forecast()

    text = []

    for day in result:
        text.append(
            f"{day.forecast_timestamp.date()} : {day.predicted_complaints:.2f}"
        )

    return "\n".join(text)