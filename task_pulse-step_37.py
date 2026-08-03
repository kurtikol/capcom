# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: TaskPulse
import unittest


class TestTaskPulse(unittest.TestCase):
    def test_add_task(self):
        from task_pulse import TaskManager
        tm = TaskManager()
        self.assertEqual(tm.tasks, [])
        tm.add({"title": "T1", "priority": 2})
        self.assertEqual(len(tm.tasks), 1)
        self.assertEqual(tm.tasks[0]["title"], "T1")

    def test_add_task_duplicate_title(self):
        from task_pulse import TaskManager
        tm = TaskManager()
        tm.add({"title": "Same", "priority": 1})
        tm.add({"title": "Same", "priority": 3})
        self.assertEqual(len(tm.tasks), 1)

    def test_add_tag(self):
        from task_pulse import TagManager
        tgm = TagManager()
        self.assertEqual(tgm.tags, [])
        tag = tgm.create("urgent")
        self.assertIn(tag, tgm.tags)
        tgm.add_tag_to_task(0, "urgent")
        self.assertEqual(tm.tasks[0]["tags"], ["urgent"])

    def test_add_priority(self):
        from task_pulse import PriorityManager
        pm = PriorityManager()
        p1 = {"title": "P1", "priority": 5}
        p2 = {"title": "P2", "priority": 3}
        self.assertEqual(pm.sort_tasks([p1, p2])[0]["title"], "P1")

    def test_add_daily_log(self):
        from task_pulse import DailyLog
        dl = DailyLog("2025-08-25")
        dl.add_entry({"task_id": 0, "note": "done"})
        self.assertEqual(len(dl.entries), 1)
        self.assertEqual(dl.entries[0]["note"], "done")


if __name__ == "__main__":
    unittest.main()
