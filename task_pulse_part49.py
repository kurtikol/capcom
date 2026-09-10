# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: TaskPulse
def final_check():
    tasks = load_tasks()
    tags = load_tags()
    logs = load_logs()
    assert len(tasks) > 0, "No tasks created"
    assert len(tasks) > 0, "No tags created"
    assert len(logs) > 0, "No logs created"
    print("✅ TaskPulse is ready! Tasks:", len(tasks), "Tags:", len(tags), "Logs:", len(logs))
