# === Stage 20: Добавь восстановление записей из архива ===
# Project: TaskPulse
def restore_from_archive():
    import json, os, datetime
    archive_path = "task_pulse_data.json"
    if not os.path.exists(archive_path): return None
    try:
        with open(archive_path) as f: data = json.load(f)
    except Exception: return None
    today = datetime.date.today().isoformat()
    existing_keys = set(d.get("id") for d in data.get("tasks", []))
    restored_count = 0
    new_tasks = [d for d in data.get("tasks", []) if d.get("id") not in existing_keys]
    for task in new_tasks:
        task["restored"] = True
        task["restored_at"] = today
        data.setdefault("journal", []).append({"date": today, "event": f"Восстановлена задача {task['title']}", "type": "restore"})
    if new_tasks:
        with open("task_pulse_data.json", "w") as f: json.dump(data, f, ensure_ascii=False, indent=2)
        return {"restored_count": len(new_tasks), "tasks": new_tasks}
    return None
