# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: TaskPulse
def init_demo_data():
    tasks = [
        {"id": 1, "title": "Спроектировать архитектуру", "priority": 3, "tags": ["planning"], "status": "done"},
        {"id": 2, "title": "Настроить базу данных", "priority": 2, "tags": ["infra"], "status": "pending"},
        {"id": 3, "title": "Написать тесты для модуля auth", "priority": 1, "tags": ["testing"], "status": "pending"},
    ]
    logs = [
        {"date": "2023-10-27", "action": "Запуск приложения", "details": "Инициализация TaskPulse"},
        {"date": "2023-10-28", "action": "Добавлена задача", "details": "Спроектировать архитектуру (приоритет 3)"},
    ]
    return tasks, logs

if __name__ == "__main__":
    print("Загрузка демонстрационных данных...")
    demo_tasks, demo_logs = init_demo_data()
    print(f"Добавлено задач: {len(demo_tasks)}")
    print(f"Записей в журнале: {len(demo_logs)}")
    print("Готово!")
