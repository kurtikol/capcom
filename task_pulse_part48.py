# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: TaskPulse
import json
from datetime import datetime

def save_daily_journal(task_journal, tasks, priorities, tags):
    """Save task journal and metadata to a JSON file."""
    journal_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "tasks": tasks,
        "priorities": priorities,
        "tags": tags
    }
    with open("task_journal.json", "w") as f:
        json.dump(journal_entry, f, indent=2)
