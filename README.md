# PyCoach Web — Local-First Python Learning Companion

A minimal, local-first web app to help beginners learn Python via micro-lessons, hands-on practice, spaced-repetition flashcards, and a Coach panel powered by **Ollama (Mistral)**.

**Note:** This app uses Ollama locally for the AI coach. Claude Sonnet 4.5 is used only as a development assistant in VS Code (not in production).

## ✨ Features

- **Micro-lessons**: Learn Python basics with runnable examples and practice challenges
- **Practice Playground**: Execute Python code directly in the browser with instant feedback
- **Flashcards with SRS**: Spaced repetition system for memorization (SM-2 algorithm)
- **Learning Log**: Track your progress in YAML format
- **AI Coach**: Ask questions to Ollama (Mistral) running locally

## 🧰 Tech Stack

- Python 3.11+
- Flask (web framework) + Jinja2 (templates)
- YAML / JSONL (local storage)
- Ollama (local AI)
- python-dotenv (environment configuration)

## 🗂 Project Structure

```
python-platform/
├── app/
│   ├── __init__.py           # Exports create_app
│   └── web/
│       ├── __init__.py       # Flask app factory
│       ├── main.py           # Entry point
│       ├── routes/           # Route blueprints
│       ├── templates/        # Jinja2 HTML templates
│       └── static/           # CSS assets
├── core/
│   ├── flashcards.py         # Flashcard CRUD + SRS
│   ├── lessons.py            # Lesson registry
│   ├── practice.py           # Code execution
│   ├── srs.py                # SM-2 scheduling
│   ├── storage.py            # YAML/JSONL utilities
│   └── log.py                # Learning log
├── data/                     # Local data files
│   ├── cards.jsonl
│   ├── learning_log.yml
│   └── progress.json
├── tests/
│   └── test_flashcards.py    # SRS tests
├── .env                      # Environment config
├── requirements.txt          # Python dependencies
└── init_data.py              # Initialize data files
```

## 🚀 Quick Start

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize Data Files

```bash
python init_data.py
```

This creates:
- `data/cards.jsonl` - Seed flashcards
- `data/learning_log.yml` - Learning log
- `data/progress.json` - Progress tracking

### 4. Configure Environment

The `.env` file should contain:

```env
ENGINE=ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=mistral
```

### 5. Install and Run Ollama (Optional)

For the Coach feature to work:

```bash
# Install Ollama from https://ollama.ai/
# Pull the Mistral model
ollama pull mistral
# Start Ollama (runs in background)
ollama serve
```

### 6. Run the Application

```bash
flask --app app.web.main run --debug
```

Visit: **http://127.0.0.1:5000**

## 🧪 Testing

Run the SRS tests:

```bash
python tests/test_flashcards.py
```

## 📖 Usage Guide

### Home Page
Welcome page with navigation to all features.

### Learn (`/learn`)
Browse micro-lessons covering:
- Variables & Types
- Lists & Methods
- Functions & Return

Each lesson includes example code and a practice challenge.

### Practice (`/practice`)
Write and execute Python code in the browser. Get instant feedback on errors or output.

### Flashcards (`/flashcards`)
Review due flashcards using spaced repetition. Grade each card (1-5) to schedule the next review:
- **1-2**: Again soon
- **3**: Good (moderate interval)
- **4-5**: Easy (longer interval)

### Coach (`/coach`)
Ask Python questions to the local Ollama AI. If Ollama is not running, you'll see a friendly error message.

## 📂 Data Files

### `data/cards.jsonl`
One JSON object per line:
```json
{"id":"card-abc123", "topic":"lists", "front":"What does list.append(x) do?", "back":"Adds x to the end of the list.", "tags":["lists","methods"], "difficulty":1, "ease_factor":2.5, "interval_days":1, "next_review_at":"2026-01-10"}
```

### `data/learning_log.yml`
YAML list of learning entries:
```yaml
- date: '2026-01-10'
  topic: variables
  concept: assignment
  snippet: 'x = 42'
  new_terms: ['variable', 'integer']
  next_actions: ['practice loops']
```

### `data/progress.json`
Simple progress counters:
```json
{"streak": 0, "lessons_completed": 0}
```

## 🛠 Development

### Code Style
- PEP 8 compliant
- Type hints where reasonable
- Docstrings for public functions

### Architecture
- **Web layer**: `app/web` - Flask routes and templates
- **Business logic**: `core` - Reusable modules
- **Storage**: `data` - Local-first YAML/JSONL files

## 🔐 Privacy

All data is stored locally in the `data/` directory. No external services except Ollama (runs on your machine).

## 🚧 Roadmap

- [ ] Add more lessons (loops, dictionaries, classes)
- [ ] Track lesson completion in progress.json
- [ ] Add practice challenges with test cases
- [ ] Export/import learning log
- [ ] Optional cloud sync

## 📝 License

See `License` file.

## 🙋 Questions?

Ask the Coach! (Make sure Ollama is running)
