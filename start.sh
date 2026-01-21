#!/usr/bin/env bash
# Start script for local development of python-platform
set -euo pipefail

# Move into repo root (script may be called from anywhere)
cd "$(dirname "$0")"

# Activate venv if present
if [ -f "venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source venv/bin/activate
fi

# Ensure PYTHONPATH includes project root so imports like `app` resolve
export PYTHONPATH="$(pwd)":${PYTHONPATH:-}

# Default Flask app entry
export FLASK_APP=app.web.main
export FLASK_ENV=development

echo "Starting webapp (FLASK_APP=$FLASK_APP) on http://127.0.0.1:5000"
flask run --host=127.0.0.1 --port=5001