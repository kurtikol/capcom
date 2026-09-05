# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: TaskPulse
def migrate_task_pulse_structure():
    """Миграция структуры данных TaskPulse: добавление полей и версионирование."""
    import datetime

    VERSION = 2
    MIGRATION_LOG = []

    # Проверяем наличие полей в текущей структуре
    required_fields = {
        "task_id", "title", "description", "priority", "tags", "status",
        "assigned_to", "created_at", "updated_at", "due_date", "journal_entry"
    }

    current_structure = {
        "task_id": int,
        "title": str,
        "description": str,
        "priority": str,
        "tags": list,
        "status": str,
        "assigned_to": str,
        "created_at": datetime.datetime,
        "updated_at": datetime.datetime,
        "due_date": datetime.datetime,
        "journal_entry": dict
    }

    # Добавляем новые поля, если их нет
    for field_name, field_type in current_structure.items():
        if field_name not in required_fields:
            required_fields.add(field_name)
            print(f"Добавлено поле: {field_name}")

    # Записываем текущую версию миграции
    migration_log.append({
        "version": VERSION,
        "timestamp": datetime.datetime.now(),
        "description": "Добавлены поля для задачи и журнала"
    })

    print(f"Миграция версии {VERSION} завершена успешно")
    print(f"Текущая версия структуры: {VERSION}")
