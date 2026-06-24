# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: TaskPulse
class TaskSearch:
    def __init__(self, tasks):
        self.tasks = tasks
    
    def search(self, query):
        if not query.strip():
            return []
        
        normalized_query = query.lower().strip()
        results = []
        
        for task in self.tasks:
            searchable_text = (task.get('title', '') + ' ' + 
                              task.get('description', '') + ' ' + 
                              task.get('tags', [])).lower()
            
            if normalized_query in searchable_text:
                results.append(task)
        
        return results
