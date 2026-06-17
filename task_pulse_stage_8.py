# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: TaskPulse
def main():
    tasks = []
    logs = []
    while True:
        print("\n=== TaskPulse ===")
        print("1. Добавить задачу | 2. Список задач | 3. Журнал | 4. Выход")
        try:
            choice = input("Выберите действие (1-4): ").strip()
        except KeyboardInterrupt:
            break
        
        if choice == "1":
            print("\n--- Добавление задачи ---")
            title = input("Название: ") or "Без названия"
            priority = input("Приоритет (Низкий/Средний/Высокий): ").strip() or "Средний"
            tag = input("Тег: ") or "Общее"
            tasks.append({"title": title, "priority": priority, "tag": tag})
            print(f"Задача '{title}' добавлена.")
        elif choice == "2":
            if not tasks:
                print("\nСписок задач пуст.")
            else:
                for i, t in enumerate(tasks):
                    print(f"{i+1}. [{t['priority']}] {t['tag']} - {t['title']}")
        elif choice == "3":
            if not logs:
                print("\nЖурнал событий пуст.")
            else:
                for entry in logs[-5:]:
                    print(f"[{entry['time']}] {entry['msg']}")
        elif choice == "4":
            print("Завершение работы...")
            break
        
        if tasks or len(logs) > 0:
            log_msg = f"Действие выполнено. Всего задач: {len(tasks)}."
            logs.append({"time": time.strftime("%H:%M"), "msg": log_msg})

if __name__ == "__main__":
    main()
