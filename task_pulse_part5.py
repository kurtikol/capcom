# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TaskPulse
def remove_task(task_id: int) -> bool:
    if not tasks or task_id < 1 or task_id > len(tasks):
        print(f"Ошибка: задача с ID {task_id} не найдена.")
        return False
    
    for i, t in enumerate(tasks):
        if t['id'] == task_id:
            del tasks[i]
            save_to_file()
            print(f"Задача #{task_id} успешно удалена.")
            return True
    
    print(f"Ошибка: задача с ID {task_id} не найдена в списке.")
    return False
