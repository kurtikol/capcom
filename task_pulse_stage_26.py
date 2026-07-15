# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: TaskPulse
def demo():
    """Quick manual test: create tasks, tags, priorities and log entries."""
    # ── 1. Tasks with priorities & tags ───────────────────────
    tasks = [
        {"id": "t0", "title": "Buy groceries", "priority": 3, "tags": ["errand"], "done": False},
        {"id": "t1", "title": "Write report", "priority": 1, "tags": ["work","urgent"], "done": True},
        {"id": "t2", "title": "Fix bug in TaskPulse", "priority": 2, "tags": ["code","bug"], "done": False},
        {"id": "t3", "title": "Plan weekend trip", "priority": 4, "tags": ["fun"], "done": True},
    ]

    # ── 2. Daily journal entries ──────────────────────────────
    log = [
        {"date": "2025-12-10", "entries": [
            "Wrote first draft of TaskPulse.",
            "Added priority levels and tags.",
            "Found a bug in task display – fixed it.",
        ]},
        {"date": "2025-12-11", "entries": [
            "Refactored file into single module.",
            "Created demo tasks for quick testing.",
        ]},
    ]

    # ── 3. Print a summary ───────────────────────────────────
    print("=== TaskPulse Demo ===")
    for i, t in enumerate(tasks):
        status = "✅ done" if t["done"] else "⬜ pending"
        tag_str = ", ".join(t["tags"]) or "(none)"
        print(f"{i+1}. [{t['id']}] {status} | P={t['priority']} | tags=[{tag_str}] -> {t['title']}")

    print()
    for entry in log:
        print(f"[{entry['date']}]")
        for line in entry["entries"]:
            print(f"  • {line}")
