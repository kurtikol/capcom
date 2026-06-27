# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: TaskPulse
def calculate_weekly_stats(tasks, log_entries):
    from datetime import date, timedelta
    if not tasks: return {}
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    week_dates = [start_of_week + timedelta(days=i) for i in range(7)]
    stats = {d.strftime('%Y-%m-%d'): {'total': 0, 'high_priority': 0, 'completed': 0} for d in week_dates}
    for task in tasks:
        if not isinstance(task.get('created_at'), date): continue
        try:
            created_date = date.fromisoformat(task['created_at'].split('T')[0])
        except (ValueError, AttributeError): continue
        if created_date < start_of_week or created_date > today: continue
        stats[created_date.strftime('%Y-%m-%d')]['total'] += 1
        if task.get('priority', 'medium') == 'high':
            stats[created_date.strftime('%Y-%m-%d')]['high_priority'] += 1
        if task.get('status') == 'completed':
            stats[created_date.strftime('%Y-%m-%d')]['completed'] += 1
    for entry in log_entries:
        try:
            date_str = entry['timestamp'].split('T')[0]
            created_date = date.fromisoformat(date_str)
        except (ValueError, AttributeError): continue
        if created_date < start_of_week or created_date > today: continue
        stats[created_date.strftime('%Y-%m-%d')]['total'] += 1
    return stats
