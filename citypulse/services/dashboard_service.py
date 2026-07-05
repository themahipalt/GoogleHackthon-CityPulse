from citypulse.database.dashboard_repository import DashboardRepository
from citypulse.schemas.dashboard import DashboardResponse


class DashboardService:

    def __init__(self):

        self.repository = DashboardRepository()

    async def get_dashboard(self):

        return DashboardResponse(

            total_complaints=self.repository.get_total_complaints(),

            high_severity=self.repository.get_high_severity(),

            top_ward=self.repository.get_top_ward(),

            forecast=self.repository.get_forecast()

        )