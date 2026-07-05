from citypulse.cloud.forecast import ForecastClient

client = ForecastClient()

forecast = client.get_forecast()

print()

print("=" * 50)
print("7 Day Complaint Forecast")
print("=" * 50)

for day in forecast:

    print(
        f"{day.forecast_timestamp.date()}  "
        f"{day.predicted_complaints:.2f}"
    )