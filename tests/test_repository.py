from citypulse.database.init_db import init_db
from citypulse.database.repository import ComplaintRepository
from citypulse.graders.schemas import (
    ComplaintReport,
    TriageResult,
    ComplaintCategory,
    Severity,
)

init_db()

def test_save_complaint():

    repo = ComplaintRepository()

    complaint = ComplaintReport(
        report_id="TEST001",
        raw_text="Huge pothole near MG Road",
        image_url=None,
        latitude=12.97,
        longitude=77.59,
        ward="Ward 5",
    )

    repo.save_complaint(complaint)

    saved = repo.get_complaint("TEST001")

    assert saved is not None
    assert saved["report_id"] == "TEST001"
    assert saved["raw_text"] == "Huge pothole near MG Road"
    assert saved["ward"] == "Ward 5"

    def test_save_triage_result():
        repo = ComplaintRepository()
    
        result = TriageResult(
            report_id="TEST001",
            category=ComplaintCategory.POTHOLE,
            severity=Severity.HIGH,
            confidence=0.98,
            rationale="Large pothole causing accidents",
        )
    
        repo.save_triage_result(result)

