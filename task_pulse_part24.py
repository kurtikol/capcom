# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: TaskPulse
def show_task_detail(task):
    if not task:
        print("Задача не найдена.")
        return
    print(f"ID: {task['id']}")
    print(f"Название: {task['title']}")
    print(f"Описание: {task.get('description', 'Без описания')}")
    print(f"Статус: {'✅' if task['status'] == 'done' else '⏳'} {task['status'].capitalize()}")
    print(f"Приоритет: {'🔴' if task['priority'] == 3 else '🟡' if task['priority'] == 2 else '🟢'} {task['priority']}")
    print(f"Теги: {', '.join(task.get('tags', [])) or '-'}")
    print(f"Создана: {task.get('created_at', '-')}")
    if 'updated_by' in task and task['updated_by']:
        print(f"Обновлено пользователем: {task['updated_by']}")
