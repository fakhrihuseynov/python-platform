"""Initialize data files for PyCoach."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from core.flashcards import ensure_seed

def init_data():
    """Initialize data directory and seed files."""
    data_dir = ROOT / "data"
    data_dir.mkdir(exist_ok=True)
    
    # Initialize flashcards
    ensure_seed()
    
    # Initialize learning log if it doesn't exist
    log_file = data_dir / "learning_log.yml"
    if not log_file.exists():
        log_file.write_text("# Learning Log - YAML entries\n")
    
    # Initialize progress file if it doesn't exist
    progress_file = data_dir / "progress.json"
    if not progress_file.exists():
        progress_file.write_text('{"streak": 0, "lessons_completed": 0}\n')
    
    print("✓ Data files initialized successfully!")
    print(f"  - {data_dir / 'cards.jsonl'}")
    print(f"  - {data_dir / 'learning_log.yml'}")
    print(f"  - {data_dir / 'progress.json'}")

if __name__ == "__main__":
    init_data()
