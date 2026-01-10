import os
import requests
from flask import Blueprint, render_template, request

bp = Blueprint("coach", __name__)

def _ollama_url():
    return os.environ.get("OLLAMA_URL", "http://localhost:11434")

def _ollama_model():
    return os.environ.get("OLLAMA_MODEL", "mistral")

@bp.route("/", methods=["GET", "POST"])
def coach():
    reply = None
    prompt = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            try:
                resp = requests.post(
                    f"{_ollama_url()}/api/generate",
                    json={"model": _ollama_model(), "prompt": prompt},
                    timeout=30,
                )
                data = resp.json()
                reply = data.get("response") or data.get("message") or str(data)
            except Exception as e:
                reply = f"Error contacting Ollama: {e}"
    return render_template("coach.html", prompt=prompt, reply=reply)
