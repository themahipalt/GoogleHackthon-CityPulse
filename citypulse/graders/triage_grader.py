from citypulse.graders.schemas import TriageResult, TriageScore


def grade_triage(predicted: TriageResult, ground_truth: dict) -> TriageScore:
    """
    ground_truth = {"category": "pothole", "severity": "high"}
    Deterministic scoring: category = 0.6 weight, severity = 0.4 weight
    """
    category_correct = predicted.category.value == ground_truth["category"]
    severity_correct = predicted.severity.value == ground_truth["severity"]

    score = 0.0
    if category_correct:
        score += 0.6
    if severity_correct:
        score += 0.4

    # penalty: agar confidence high hai but answer galat hai, extra penalty
    if not category_correct and predicted.confidence > 0.8:
        score -= 0.1

    score = max(0.0, min(1.0, score))

    return TriageScore(
        report_id=predicted.report_id,
        score=score,
        category_correct=category_correct,
        severity_correct=severity_correct,
        notes=f"category={'ok' if category_correct else 'wrong'}, severity={'ok' if severity_correct else 'wrong'}",
    )