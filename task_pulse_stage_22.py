# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: TaskPulse
def check_overdue_reminders():
    """Проверяет просроченные напоминания и возвращает список с информацией о них."""
    overdue = []
    
    for task in tasks:
        if task.get('reminder') and task['status'] == 'pending':
            reminder_time = datetime.fromisoformat(task['reminder'])
            if reminder_time <= datetime.now():
                overdue.append({
                    'task_id': task['id'],
                    'title': task['title'],
                    'reminder_time': task['reminder'],
                    'days_overdue': (datetime.now() - reminder_time).days + 1
                })
    
    return overdue

def display_overdue_reminders():
    """Отображает список просроченных напоминаний в формате отчета."""
    overdue = check_overdue_reminders()
    
    if not overdue:
        print("\n✅ Все напомнения в срок!")
        return
    
    print(f"\n⚠️  Просрочено {len(overdue)} напоминание{'й' if len(overdue) == 1 else 'ий' if len(overdue) > 1 else ''}(-{'ых' if len(overdue) != 2 else 'го'})!")
    print("-" * 50)
    
    for i, item in enumerate(overdue, 1):
        days_str = f"{item['days_overdue']} дн." if item['days_overdue'] == 1 else f"{item['days_overdue']} дней"
        print(f"{i}. [{task.get('title', 'Без названия')}] — просрочено на {days_str}")

# Пример использования:
# check_overdue_reminders()
# display_overdue_reminders()
