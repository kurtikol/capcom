# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: TaskPulse
def filter_tasks(status=None, category=None, tags=None):
    if status is not None:
        tasks = [t for t in tasks if t.get('status') == status]
    if category is not None:
        tasks = [t for t in tasks if t.get('category') == category]
    if tags is not None:
        task_tags = {tag.lower() for tag in tags}
        tasks = [t for t in tasks if any(tag.lower() in t.get('tags', []) for tag in task_tags)]
    return tasks
