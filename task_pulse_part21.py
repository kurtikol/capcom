# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: TaskPulse
import json
from datetime import date, timedelta

def add_reminder(tasks_db_path="tasks.json", reminder_data=None):
    """Добавляет напоминание в базу задач и возвращает его ID."""
    if not reminder_data:
        return None
    tasks = load_tasks(tasks_db_path)
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": f"Напоминание: {reminder_data.get('text', 'Без описания')}",
        "due_date": reminder_data["date"],
        "priority": "high",
        "tag": "reminders",
        "status": "pending",
        "created_at": date.today().isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks_db_path, tasks)
    return task_id

def load_tasks(path="tasks.json"):
    if path not in globals() or not os.path.exists(path):
        return []
