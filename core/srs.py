
from datetime import datetime, timedelta

def update_schedule(card, grade: int):
    ef = max(1.3, float(card.get("ease_factor", 2.5)))
    interval = int(card.get("interval_days", 1))

    if grade < 3:
        interval = 1
        ef = max(1.3, ef - 0.2)
    else:
        ef = ef + 0.1
        interval = max(1, round(interval * ef))

    next_review = datetime.now() + timedelta(days=interval)
    card["ease_factor"] = round(ef, 2)
    card["interval_days"] = interval
    card["next_review_at"] = next_review.strftime("%Y-%m-%d")
    return card
