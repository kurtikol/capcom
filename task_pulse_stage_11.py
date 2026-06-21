# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: TaskPulse
import json, os

DATA_FILE = "tasks_pulse.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"tasks": [], "journal": []}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"tasks": [], "journal": []}

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True) if os.path.dirname(DATA_FILE) else None
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
