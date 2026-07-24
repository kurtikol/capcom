# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: TaskPulse
def switch_profile(profile_id: str) -> dict:
    """Переключить активный профиль по id."""
    if profile_id not in _profiles:
        return {"error": "Профиль не найден"}
    current = _active_profile.get("id")
    if current is None or current == profile_id:
        return {"message": "Текущий профиль уже выбран"}
    _active_profile["id"] = profile_id
    for t in _tasks:
        t["user_profile_id"] = profile_id
    return {
        "current_profile": _profiles[profile_id],
        "previous_profile": _profiles.get(current),
    }
