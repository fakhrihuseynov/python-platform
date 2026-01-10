
from datetime import datetime
from .storage import append_yaml

def add_log(topic: str, concept: str, snippet: str, new_terms=None, next_actions=None):
    entry = {
      "date": datetime.now().strftime("%Y-%m-%d"),
      "topic": topic,
      "concept": concept,
      "snippet": snippet,
      "new_terms": new_terms or [],
      "next_actions": next_actions or [],
    }
    append_yaml("learning_log.yml", entry)
