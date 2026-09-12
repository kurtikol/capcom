# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: TaskPulse
# TaskPulse – финальная полировка: улучшенные сообщения и комментарии
def _format_task(task):
    """Форматирование задачи для отображения в журнале."""
    return (
        f"[{task['id']}] "
        f"{'🔴' if task['priority'] == 'high' else '🟡' if task['priority'] == 'medium' else '🟢'} "
        f"{task['title']} ({task['status']})"
    )

def _format_day_summary(day):
    """Форматирование ежедневного отчёта."""
    return (
        f"📅 {day['date']}:\n"
        f"  • Добавлено задач: {len(day['added'])}\n"
        f"  • Завершено задач: {len(day['completed'])}\n"
        f"  • Теги за день: {', '.join(set(tag for task in day['added'] + day['completed'] for tag in task.get('tags', []))) or 'нет'}"
    )

def _format_journal(journal):
    """Форматирование полного журнала."""
    lines = ["📖 Журнал TaskPulse:\n"]
    for day in journal:
        lines.append(_format_day_summary(day))
        lines.append("-" * 30)
    return "\n".join(lines)
