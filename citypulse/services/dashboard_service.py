from citypulse.database.dashboard_repository import DashboardRepository


class DashboardService:

    def __init__(self):

        self.repository = DashboardRepository()

    async def get_dashboard(self):

        return {
            "total_complaints": self.repository.get_total_complaints(),
            "high_severity": self.repository.get_high_severity(),
            "top_ward": self.repository.get_top_ward(),
            "forecast": self.repository.get_forecast()
        }

    async def get_trend(self):

        return self.repository.get_trend()