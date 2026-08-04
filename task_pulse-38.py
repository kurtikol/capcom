# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: TaskPulse
import unittest

class TestTaskPulseEdgeCases(unittest.TestCase):

    def test_empty_task_no_tags(self):
        task = Task(title="Empty", description="", priority=1)
        self.assertEqual(task.tags, [])
        self.assertTrue(task.is_complete())

    def test_high_priority_low_number(self):
        tasks = [
            Task("Low", 5), Task("High", 1), Task("Critical", 0)
        ]
        sorted_tasks = sort_tasks(tasks)
        self.assertEqual([t.title for t in sorted_tasks], ["Critical", "High", "Low"])

    def test_duplicate_tags(self):
        task = Task(title="Dup Tags", description="", priority=1, tags=["urgent", "work"])
        task.tags.append("urgent")
        self.assertEqual(task.get_unique_tags(), 2)

    def test_sort_stability(self):
        tasks = [Task(f"task_{i}", i % 3, ["t"] * (i % 5)) for i in range(10)]
        sorted_tasks = sort_tasks(tasks)
        self.assertEqual([t.title for t in sorted_tasks], [f"task_{i}" for i in range(10)])

    def test_task_complete_with_description(self):
        task = Task(title="Done", description="Some work", priority=2, tags=["done"])
        task.complete()
        self.assertTrue(task.is_complete())
        self.assertEqual(task.description, "Some work")

if __name__ == "__main__":
    unittest.main()
