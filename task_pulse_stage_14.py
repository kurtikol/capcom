# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: TaskPulse
def generate_summary(tasks, logs):
    if not tasks: return "Нет задач."
    priorities = {"high": 0, "medium": 0, "low": 0}
    for t in tasks: priorities[t.get("priority", "low")] += 1
    tags_count = {}
    for t in tasks:
        for tag in t.get("tags", []): tags_count[tag] = tags_count.get(tag, 0) + 1
    today_logs = [l for l in logs if l.get("date") == "сегодня"] or []
    summary_lines = [f"Всего задач: {len(tasks)}"]
    summary_lines.append(f"По приоритетам: высокие={priorities['high']}, средние={priorities['medium']}, низкие={priorities['low']}")
    if tags_count:
        top_tags = sorted(tags_count.items(), key=lambda x: x[1], reverse=True)[:3]
        summary_lines.append(f"Популярные теги: {', '.join([f'{t} ({c})' for t, c in top_tags])}")
    if today_logs:
        summary_lines.append(f"Записей в журнале сегодня: {len(today_logs)}")
    else:
        summary_lines.append("Сегодня записей в журнале нет.")
    return "\n".join(summary_lines)
