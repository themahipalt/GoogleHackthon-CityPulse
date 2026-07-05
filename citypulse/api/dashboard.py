from fastapi import APIRouter

from citypulse.services.dashboard_service import DashboardService

router = APIRouter()

service = DashboardService()


@router.get("/dashboard")
async def dashboard():

    return await service.get_dashboard()