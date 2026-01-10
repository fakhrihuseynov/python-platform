import json
import os
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

def path(*parts):
    return DATA_DIR.joinpath(*parts)

def read_yaml(name):
    p = path(name)
    if not p.exists():
        return []
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []

def append_yaml(name, item):
    items = read_yaml(name)
    items.append(item)
    with open(path(name), "w", encoding="utf-8") as f:
        yaml.safe_dump(items, f, allow_unicode=True)

def read_jsonl(name):
    p = path(name)
    if not p.exists():
        return []
    with open(p, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def write_jsonl(name, items):
    with open(path(name), "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
