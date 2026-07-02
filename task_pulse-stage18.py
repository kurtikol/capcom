# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: TaskPulse
class TagManager:
    def __init__(self):
        self.tags = {}  # {tag_name: count}
    
    def add_tag(self, task_id: str, tag: str) -> bool:
        if not tag.strip(): return False
        current_count = self.tags.get(tag, 0)
        new_count = current_count + 1
        self.tags[tag] = new_count
        
        # Обновляем список тегов задачи в основном хранилище задач (предполагается глобальная переменная tasks_db или аналогичный доступ)
        if not hasattr(self, '_tasks_db'):
            return False
            
        task = self._tasks_db.get(task_id)
        if task:
            existing_tags = set(task.get('tags', []))
            existing_tags.add(tag)
            task['tags'] = list(existing_tags)
            
        # Удаляем дубликаты при добавлении (если тег уже был, просто увеличиваем счетчик для статистики или логики удаления)
        return True
    
    def remove_tag(self, task_id: str, tag: str) -> bool:
        if not self.tags.get(tag, 0): return False
        
        # Уменьшаем глобальный счетчик тега
        self.tags[tag] -= 1
        if self.tags[tag] == 0: del self.tags[tag]
        
        task = self._tasks_db.get(task_id)
        if not task or 'tags' not in task: return False
        
        existing_tags = set(task['tags'])
        if tag in existing_tags:
            existing_tags.remove(tag)
            task['tags'] = list(existing_tags)
            
        # Если после удаления список тегов пуст, можно убрать ключ или оставить пустой список по желанию
        if not existing_tags:
            del task['tags']
            
        return True
    
    def get_tag_count(self, tag: str) -> int:
        return self.tags.get(tag, 0)
