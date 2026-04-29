import json
from task import Task

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Task.from_dict(task) for task in data]
    except FileNotFoundError:
        # якщо файлу нема — створюємо
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump([], file)
        return []
    
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4, ensure_ascii=False)