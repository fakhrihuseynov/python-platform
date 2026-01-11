import os
import requests
import markdown
from flask import Blueprint, render_template, request
from markupsafe import Markup

bp = Blueprint("coach", __name__)

def _ollama_url():
    return os.environ.get("OLLAMA_URL", "http://localhost:11434")

def _ollama_model():
    return os.environ.get("OLLAMA_MODEL", "mistral")

@bp.route("/", methods=["GET", "POST"])
def coach():
    reply = None
    reply_html = None
    prompt = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            try:
                resp = requests.post(
                    f"{_ollama_url()}/api/generate",
                    json={"model": _ollama_model(), "prompt": prompt, "stream": False},
                    timeout=60,
                )
                resp.raise_for_status()
                data = resp.json()
                reply = data.get("response", "")
                if not reply:
                    reply = f"No response received. Full data: {data}"
                else:
                    # Convert markdown to HTML
                    md = markdown.Markdown(extensions=['fenced_code', 'codehilite', 'tables', 'nl2br'])
                    reply_html = Markup(md.convert(reply))
            except requests.exceptions.ConnectionError:
                reply = "Could not connect to Ollama. Make sure it's running:\n\n1. Install Ollama from https://ollama.ai/\n2. Run: ollama pull mistral\n3. Start: ollama serve"
            except Exception as e:
                reply = f"Error contacting Ollama: {e}"
    return render_template("coach.html", prompt=prompt, reply=reply, reply_html=reply_html)
