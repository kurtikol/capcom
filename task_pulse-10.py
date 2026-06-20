# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: TaskPulse
def export_state_to_json():
    import json
    from datetime import datetime
    state = {
        "tasks": tasks,
        "tags": tags,
        "journal": journal,
        "exported_at": datetime.now().isoformat(),
        "task_count": len(tasks),
        "tag_count": len(tags)
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
