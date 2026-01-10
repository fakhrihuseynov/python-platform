import uuid
from datetime import datetime
from .storage import read_jsonl, write_jsonl
from .srs import update_schedule

CARDS_FILE = "cards.jsonl"

def _load_cards():
    return read_jsonl(CARDS_FILE)

def _save_cards(cards):
    write_jsonl(CARDS_FILE, cards)

def ensure_seed():
    cards = _load_cards()
    if not cards:
        cards = [
            {"id": "card-"+uuid.uuid4().hex, "topic":"lists",
             "front":"What does list.append(x) do?",
             "back":"Adds x to the end of the list.",
             "tags":["lists","methods"], "difficulty":1,
             "ease_factor":2.5, "interval_days":1,
             "next_review_at": datetime.now().strftime("%Y-%m-%d")},
            {"id": "card-"+uuid.uuid4().hex, "topic":"functions",
             "front":"What does return do in a function?",
             "back":"It exits the function and gives a value to the caller.",
             "tags":["functions","return"], "difficulty":1,
             "ease_factor":2.5, "interval_days":1,
             "next_review_at": datetime.now().strftime("%Y-%m-%d")},
        ]
        _save_cards(cards)

def load_due_cards():
    ensure_seed()
    today = datetime.now().strftime("%Y-%m-%d")
    cards = [c for c in _load_cards() if c.get("next_review_at", today) <= today]
    return cards[:7]

def grade_card(card_id: str, grade: int):
    cards = _load_cards()
    for c in cards:
        if c["id"] == card_id:
            update_schedule(c, grade)
            break
    _save_cards(cards)
