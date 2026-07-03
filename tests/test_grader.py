import pytest
from citypulse.graders.schemas import TriageResult, ComplaintCategory, Severity
from citypulse.graders.triage_grader import grade_triage


def test_perfect_match():
    predicted = TriageResult(
        report_id="r1", category=ComplaintCategory.POTHOLE,
        severity=Severity.HIGH, confidence=0.9, rationale="test",
    )
    ground_truth = {"category": "pothole", "severity": "high"}
    result = grade_triage(predicted, ground_truth)
    assert result.score == 1.0


def test_wrong_category_high_confidence_penalty():
    predicted = TriageResult(
        report_id="r2", category=ComplaintCategory.GARBAGE,
        severity=Severity.HIGH, confidence=0.95, rationale="test",
    )
    ground_truth = {"category": "pothole", "severity": "high"}
    result = grade_triage(predicted, ground_truth)
    assert result.score == pytest.approx(0.3)  # 0.4 severity - 0.1 penalty