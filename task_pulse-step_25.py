# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: TaskPulse
def parse_date(date_str):
    """Парсит дату из строки в формат 'YYYY-MM-DD'. Возвращает None при ошибке."""
    try:
        parts = date_str.strip().split('-')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            return None
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return None
        import datetime
        datetime.date(year=year, month=month, day=day)
        return date_str.strip()
    except Exception:
        return None

def format_error(msg):
    """Формирует понятное сообщение об ошибке."""
    return f"❌ Ошибка: {msg}"
