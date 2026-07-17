# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: TaskPulse
def reset_demo_data():
    """Сбросить все данные в исходное состояние (демо)"""
    global tasks, tags, journal, priorities
    tasks = [
        {"id": 1, "title": "Установить Python 3.12", "description": "Скачать и установить последнюю версию", "priority": "high", "status": "done", "tags": ["setup"], "created_at": "2026-05-01"},
        {"id": 2, "title": "Настроить IDE", "description": "VS Code + плагины для Python и Git", "priority": "high", "status": "in_progress", "tags": ["setup"], "created_at": "2026-05-01"},
        {"id": 3, "title": "Создать базу данных SQLite", "description": "Инициализировать schema и seed данные", "priority": "medium", "status": "pending", "tags": ["db"], "created_at": "2026-05-01"},
        {"id": 4, "title": "Прототип API задач", "description": "RESTful endpoints CRUD", "priority": "high", "status": "in_progress", "tags": ["api"], "created_at": "2026-05-01"},
        {"id": 5, "title": "Добавить авторизацию JWT", "description": "Reactive Auth + middleware", "priority": "medium", "status": "pending", "tags": ["auth"], "created_at": "2026-05-01"},
        {"id": 6, "title": "Написать unit-тесты", "description": "pytest для API и моделей", "priority": "low", "status": "pending", "tags": ["testing"], "created_at": "2026-05-01"},
    ]
    tags = ["setup", "db", "api", "auth", "testing", "ui"]
    priorities = {"high": 3, "medium": 2, "low": 1}
    journal = [
        {"date": "2026-05-01", "entries": ["Проект TaskPulse запущен", "Добавлен приоритет и теги"]},
        {"date": "2026-05-02", "entries": ["Дописан модуль авторизации", "Настроены unit-тесты"]},
    ]

def clear_all():
    """Полностью очистить все данные"""
    global tasks, tags, journal, priorities
    tasks = []
    tags = []
    journal = []
    priorities = {}

if __name__ == "__main__":
    reset_demo_data()
    print(f"Загружено {len(tasks)} демо-задач")
