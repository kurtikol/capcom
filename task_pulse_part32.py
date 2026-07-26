# === Stage 32: Добавь журнал действий пользователя ===
# Project: TaskPulse
from datetime import date, time, timedelta

class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action_type, message=""):
        entry_time = (date.today(), time(0, 0))
        entry = {"user": user, "action": action_type, "message": message, "timestamp": entry_time}
        self.entries.append(entry)
        return entry

    def get_log(self):
        return [
            f"{e['timestamp'][1].strftime('%H:%M')} | {e['user']} | {e['action']}: {e['message']}"
            for e in reversed(self.entries)
        ]
