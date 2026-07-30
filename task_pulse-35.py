# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: TaskPulse
def get_next_actions(task, today):
    """Возвращает краткие рекомендации на основе состояния задачи."""
    recs = []
    if task["priority"] == "critical" and not task.get("resolved"):
        recs.append(f"[КРИТИЧНО] {task['title']} — срочно завершить до конца дня")
    elif task["status"] in ("backlog", "reviewed") and not task.get("assigned_to"):
        recs.append(f"{task['title']} ещё без исполнителя — назначьте кого-то")
    if task.get("due_date") and task["due_date"].startswith(today):
        if task["status"] != "done":
            recs.append(f"{task['title']} истекает сегодня — проверьте прогресс")
    tags = [t for t in task.get("tags", [])]
    if len(tags) == 0:
        recs.append(f"{task['title']} не имеет тегов — добавьте для поиска")
    elif "urgent" not in tags and task["priority"] != "low":
        recs.append(f"{task['title']} может нуждаться в пересмотре приоритета")
    if task.get("journal") and any(j.get("action") == "review" for j in task["journal"]):
        recs.append(f"{task['title']} требует периодической оценки прогресса")
    return "\n".join(recs) if recs else "Все в порядке — продолжайте работу"
