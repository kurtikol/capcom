# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: TaskPulse
def edit_task(task_id, updates):
    if task_id not in tasks:
        print(f"Задача с ID {task_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in task_fields and value is not None:
            tasks[task_id][key] = value
        elif key == 'priority' and value not in valid_priorities:
            print(f"Недопустимый приоритет {value}. Доступны: {valid_priorities}")
            return False
    
    log_entry = f"[{datetime.now()}] Задача {task_id} отредактирована: {updates}"
    daily_log.append(log_entry)
    
    print(f"Задача {task_id} успешно обновлена.")
    return True
