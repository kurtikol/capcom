# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: TaskPulse
class TaskPulse:
    def __init__(self):
        self.tasks = []
        self.journal = {}
        self._next_id = 1

    def add_task(self, title, priority=3, tag="general"):
        task = {
            "id": self._next_id,
            "title": title,
            "priority": priority,
            "tag": tag,
            "status": "pending",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self._next_id += 1
        return task

    def log_event(self, event_type, details):
        date = time.strftime("%Y-%m-%d")
        if date not in self.journal:
            self.journal[date] = []
        entry = {
            "time": time.strftime("%H:%M:%S"),
            "type": event_type,
            "details": details
        }
        self.journal[date].append(entry)

    def get_tasks_by_priority(self):
        return sorted(self.tasks, key=lambda t: t["priority"], reverse=True)

    def get_daily_journal(self, date=None):
        if not date:
            date = time.strftime("%Y-%m-%d")
        return self.journal.get(date, [])
