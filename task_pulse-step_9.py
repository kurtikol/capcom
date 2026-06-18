# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: TaskPulse
import json, sys
try:
    initial_data = """{
        "tasks": [
            {"id": 101, "title": "Инициализация проекта", "status": "done", "priority": "high", "tags": ["setup"], "created_at": "2024-01-01T09:00:00"}
        ],
        "journal": [
            {"date": "2024-01-01", "entries": [{"time": "09:00", "text": "Запуск TaskPulse."}]}
        ]
    }"""
    with open("data.json", "w") as f:
        json.dump(json.loads(initial_data), f, ensure_ascii=False)
except Exception as e:
    print(f"Ошибка загрузки начальных данных: {e}", file=sys.stderr)
