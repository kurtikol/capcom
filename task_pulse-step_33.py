# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: TaskPulse
import time

class ActionHistory:
    def __init__(self):
        self.entries = []

    def record(self, action_name, details=None):
        self.entries.append({'name': action_name, 'details': details or '', 'time': time.time()})

    def undo_last(self):
        if not self.entries:
            return None
        last = self.entries.pop()
        return last.get('details') or last.get('action_name', '')


def add_undo_support_to_task_pulse(tasks, tags, daily_log, action_history):
    """Добавляет возможность отката последнего действия."""
    
    def undo_last_change():
        entry = action_history.undo_last()
        if not entry:
            print("Нет истории для отката.")
        else:
            print(f"Откат: {entry}")
    
    # Пример использования: откат при удалении задачи
    original_remove_task = tasks['remove_task']
    
    def remove_task_with_undo(task_id):
        if task_id in tasks:
            action_history.record('remove_task', task_id)
            del tasks[task_id]
            print(f"Задача {task_id} удалена.")
        else:
            print(f"Задача {task_id} не найдена.")
    
    return remove_task_with_undo, undo_last_change

# Пример использования
remove_task = add_undo_support_to_task_pulse(tasks, tags, daily_log, action_history)[0]
undo_func = add_undo_support_to_task_pulse(tasks, tags, daily_log, action_history)[1]


if __name__ == "__main__":
    # Демонстрация работы undo
    task_id = "task_3"
    remove_task(task_id)
    undo_func()
