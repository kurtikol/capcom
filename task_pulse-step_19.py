# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: TaskPulse
def archive_completed_tasks(tasks, cutoff_days=30):
    from datetime import datetime, timedelta
    today = datetime.now()
    cutoff_date = today - timedelta(days=cutoff_days)
    archived_count = 0
    for task in tasks:
        if task['status'] == 'completed' and task.get('created_at', '') <= cutoff_date.strftime('%Y-%m-%d'):
            task['archived'] = True
            archived_count += 1
    return archived_count

def export_archived_tasks(tasks):
    import json
    from datetime import datetime
    today = datetime.now().strftime('%Y-%m-%d')
    header = f"TaskPulse Archive Report | {today}\n{'='*50}\n\n"
    lines = [header]
    for task in tasks:
        if task.get('archived'):
            lines.append(f"[ARCHIVED] {task['title']} (ID:{task['id']}) - Completed:{task['completed_at']}, Tags:{', '.join(task.get('tags', []))}")
    return "\n".join(lines)

def cleanup_old_logs(logs, keep_days=7):
    from datetime import datetime, timedelta
    today = datetime.now()
    cutoff_date = today - timedelta(days=keep_days)
    filtered_logs = [log for log in logs if log['timestamp'] >= cutoff_date.strftime('%Y-%m-%d %H:%M:%S')]
    return filtered_logs

def process_archive(tasks, logs):
    archived_count = archive_completed_tasks(tasks)
    cleaned_logs = cleanup_old_logs(logs)
    report_text = export_archived_tasks([t for t in tasks if t.get('archived')])
    print(f"Archived {archived_count} tasks.")
    print(report_text[:200] + "..." if len(report_text) > 200 else report_text)
    return cleaned_logs
