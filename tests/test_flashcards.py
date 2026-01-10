"""Test flashcards SRS scheduling."""
import sys
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.srs import update_schedule


def test_update_schedule_fail():
    """Test that failing (grade < 3) resets interval to 1."""
    card = {"ease_factor": 2.5, "interval_days": 5, "next_review_at": "2026-01-01"}
    result = update_schedule(card, grade=1)
    
    assert result["interval_days"] == 1, "Failed review should reset interval to 1"
    assert result["ease_factor"] < 2.5, "Failed review should decrease ease_factor"
    print("✓ test_update_schedule_fail passed")


def test_update_schedule_success():
    """Test that passing (grade >= 3) increases interval."""
    card = {"ease_factor": 2.5, "interval_days": 1, "next_review_at": "2026-01-01"}
    result = update_schedule(card, grade=4)
    
    assert result["interval_days"] > 1, "Successful review should increase interval"
    assert result["ease_factor"] >= 2.5, "Successful review should increase or maintain ease_factor"
    print("✓ test_update_schedule_success passed")


def test_update_schedule_multiple_successes():
    """Test that successive successes compound interval growth."""
    card = {"ease_factor": 2.5, "interval_days": 1, "next_review_at": "2026-01-01"}
    
    # First success
    card = update_schedule(card, grade=4)
    interval_1 = card["interval_days"]
    
    # Second success
    card = update_schedule(card, grade=4)
    interval_2 = card["interval_days"]
    
    assert interval_2 > interval_1, "Successive successes should compound interval"
    print(f"✓ test_update_schedule_multiple_successes passed (1 → {interval_1} → {interval_2})")


if __name__ == "__main__":
    test_update_schedule_fail()
    test_update_schedule_success()
    test_update_schedule_multiple_successes()
    print("\nAll tests passed! ✓")
