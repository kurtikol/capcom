# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: TaskPulse
def sort_tasks(tasks, key='date'):
    if not tasks: return []
    order = {'high': 0, 'medium': 1, 'low': 2}
    reverse = {key == 'priority'}
    def _sort(t):
        val = t.get(key)
        if key == 'priority': return order.get(val, 3), -t['id']
        elif key == 'date': return val or datetime.max, -t['id']
        else: return str(t[key]).lower(), -t['id']
    return sorted(tasks, key=_sort)
