# === Stage 17: Добавь группировку записей по категориям ===
# Project: TaskPulse
def group_by_category(tasks):
    groups = {}
    for task in tasks:
        cat = task.get('category', 'Uncategorized')
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(task)
    return dict(sorted(groups.items()))
