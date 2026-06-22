# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: TaskPulse
import json, os

def load_tasks_from_file(filepath: str) -> list[dict]:
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден.")
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'tasks' in data:
            print("Читание из формата {\"tasks\": [...]}")
            return data['tasks']
        else:
            print("Неверный формат JSON данных.")
            return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return []
    except PermissionError:
        print(f"Нет прав для чтения файла {filepath}.")
        return []
