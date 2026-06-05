# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TaskPulse
class Task:
    def __init__(self, title, priority=1, tags=None):
        self.title = title
        self.priority = int(priority) if isinstance(priority, str) else priority
        self.tags = [tag.strip() for tag in tags.split(',') if tag.strip()] if isinstance(tags, str) else tags

class InputValidator:
    @staticmethod
    def validate_task_input(title, priority, tags):
        if not title or len(title.strip()) < 2:
            raise ValueError("Заголовок задачи должен быть не пустым и содержать минимум 2 символа.")
        valid_priorities = ['low', 'medium', 'high']
        if isinstance(priority, str):
            if priority.lower() not in valid_priorities:
                raise ValueError(f"Приоритет должен быть одним из: {', '.join(valid_priorities)}.")
            priority_map = {'low': 1, 'medium': 2, 'high': 3}
            return Task(title.strip(), priority_map[priority.lower()], tags)
        elif isinstance(priority, int):
            if not (1 <= priority <= 3):
                raise ValueError("Числовой приоритет должен быть от 1 до 3.")
            return Task(title.strip(), priority, tags)
        else:
            raise TypeError("Приоритет должен быть строкой или целым числом.")

    @staticmethod
    def validate_tags(tags):
        if not isinstance(tags, list):
            return [t.strip() for t in tags.split(',') if t.strip()]
        return [tag.strip() for tag in tags if tag.strip()]
