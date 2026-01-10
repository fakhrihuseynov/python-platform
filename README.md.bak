
# PyCoach Web — Local-First Python Learning Companion

A minimal, local-first web app to help beginners learn Python via micro-lessons, hands-on practice, spaced-repetition flashcards, tiny projects, and a Coach panel powered by **Ollama (Mistral)**.  
**Note:** Claude Sonnet 4.5 is used only as a *development assistant* in VS Code (not shipped in the app).

## ✨ Objectives
- Beginner-friendly, step-by-step learning with runnable examples and assert-based checks.
- Spaced Repetition Flashcards (SRS) stored locally.
- Local privacy: artifacts in `data/` (YAML/JSONL).
- **AI Coach uses Ollama (Mistral) locally**; paid agents may be added later.

## 🧰 Tech Stack
- Python 3.11+
- Flask (web) + Jinja2 (templates)
- YAML / JSONL (local storage)
- Ollama client (local) for AI coach (HTTP API)

## 🗂 Project Structure
See “Folder Structure” below. Key areas:
- `app/web` — Flask app, routes, templates, static.
- `core` — lessons, practice, flashcards (SRS), storage, coach (Ollama adapter).
- `data` — `learning_log.yml`, `cards.jsonl`, `progress.json`.

## 🚀 Quick Start (macOS)
### 1) Create & activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
