# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: TaskPulse
def demo():
    print("=== TaskPulse Demo ===\n")

    # 1. Создаем задачи
    tasks = [
        {"title": "Приветствие", "priority": 1, "tags": ["onboarding"], "done": False},
        {"title": "Анализ данных", "priority": 3, "tags": ["research"], "done": False},
        {"title": "Написать отчёт", "priority": 1, "tags": ["onboarding", "report"], "done": True},
        {"title": "Дизайн интерфейса", "priority": 2, "tags": ["design"], "done": False},
        {"title": "Тестирование", "priority": 2, "tags": ["qa"], "done": False},
        {"title": "Документация", "priority": 3, "tags": ["docs"], "done": False},
    ]

    # 2. Показываем все задачи
    print("Все задачи:")
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else "○"
        print(f"  {i}. [{status}] {t['title']} (приоритет: {t['priority']}, теги: {', '.join(t['tags'])})")

    # 3. Фильтр по приоритету
    high_priority = [t for t in tasks if t["priority"] <= 2]
    print(f"\nЗадачи с высоким приоритетом (<=2): {len(high_priority)}")
    for t in high_priority:
        print(f"  - {t['title']}")

    # 4. Фильтр по тегу
    onboarding_tasks = [t for t in tasks if "onboarding" in t["tags"]]
    print(f"\nЗадачи с тегом 'onboarding': {len(onboarding_tasks)}")
    for t in onboarding_tasks:
        print(f"  - {t['title']}")

    # 5. Подсчёт
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    pending = total - completed
    avg_priority = sum(t["priority"] for t in tasks) / total if total else 0

    print(f"\nСтатистика:")
    print(f"  Всего задач: {total}")
    print(f"  Завершено: {completed}")
    print(f"  Осталось: {pending}")
    print(f"  Средний приоритет: {avg_priority:.1f}")

    # 6. Дневной журнал
    journal = [
        {"date": "2024-01-15", "entry": "Первый день работы: все задачи в работе"},
        {"date": "2024-01-16", "entry": "Завершили 'Написать отчёт'. Осталось 5 задач."},
        {"date": "2024-01-17", "entry": "Продолжаем работу над дизайном и тестированием."},
    ]

    print(f"\nДневной журнал:")
    for entry in journal:
        print(f"  {entry['date']}: {entry['entry']}")

    print("\n=== Demo завершен ===")
