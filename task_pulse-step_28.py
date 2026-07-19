# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: TaskPulse
def compute_metrics(tasks):
    if not tasks:
        return {
            "total": 0, "completed": 0, "in_progress": 0, "pending": 0,
            "priority_distribution": {}, "tag_distribution": {}
        }
    total = len(tasks)
    completed = sum(1 for t in tasks if t["status"] == "done")
    in_progress = sum(1 for t in tasks if t["status"] == "in_progress")
    pending = total - completed - in_progress

    priority_dist = {}
    tag_dist = {}
    for t in tasks:
        p = t.get("priority", "medium")
        priority_dist[p] = priority_dist.get(p, 0) + 1
        tags = t.get("tags", [])
        for tg in tags:
            tag_dist[tg] = tag_dist.get(tg, 0) + 1

    return {
        "total": total,
        "completed": completed,
        "in_progress": in_progress,
        "pending": pending,
        "completion_rate": round(completed / total * 100, 2),
        "priority_distribution": priority_dist,
        "tag_distribution": tag_dist
    }
