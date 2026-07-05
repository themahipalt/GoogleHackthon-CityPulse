from datetime import datetime, timedelta
import random


def random_date_last_n_days(days: int = 90) -> datetime:
    """
    Returns a random datetime within the last N days.
    """

    today = datetime.now()

    random_days = random.randint(0, days)

    random_hours = random.randint(0, 23)

    random_minutes = random.randint(0, 59)

    random_seconds = random.randint(0, 59)

    return (
        today
        - timedelta(days=random_days)
        + timedelta(
            hours=random_hours,
            minutes=random_minutes,
            seconds=random_seconds,
        )
    )