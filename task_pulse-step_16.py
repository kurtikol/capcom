# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: TaskPulse
def calculate_monthly_stats(tasks, journal):
    from datetime import datetime
    stats = {}
    for task in tasks:
        if not hasattr(task, 'created_at'): continue
        date = task.created_at.date()
        month_key = f"{date.year}-{date.month}"
        if month_key not in stats:
            stats[month_key] = {'total': 0, 'completed': 0, 'priorities': {1: 0, 2: 0, 3: 0}}
        stats[month_key]['total'] += 1
        if task.status == 'done':
            stats[month_key]['completed'] += 1
        priority = getattr(task, 'priority', 1)
        stats[month_key]['priorities'][priority] += 1
    
    for entry in journal:
        if not hasattr(entry, 'timestamp'): continue
        date = entry.timestamp.date()
        month_key = f"{date.year}-{date.month}"
        if month_key not in stats:
            stats[month_key] = {'total': 0, 'completed': 0, 'priorities': {1: 0, 2: 0, 3: 0}}
        
    return stats
