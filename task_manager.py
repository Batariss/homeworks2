from task import Task
from storage import save_tasks


def get_next_id(tasks):
    """Повертає наступний ID для нової задачі"""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1


def add_task(tasks):
    """Додати нову задачу"""
    title = input("Введи назву: ")
    description = input("Введи опис: ")
    
    print("Обери пріоритет (1=low, 2=medium, 3=high):")
    priority_choice = input("Обери: ")
    priority_map = {"1": "low", "2": "medium", "3": "high"}
    priority = priority_map.get(priority_choice, "medium")

    new_task = Task(get_next_id(tasks), title, description, priority=priority)
    tasks.append(new_task)

    save_tasks(tasks)
    print("✓ Задачу додано")


def edit_task(tasks):
    """Редагувати задачу"""
    try:
        task_id = int(input("Введи ID задачі для редагування: "))
    except ValueError:
        print("✗ Це не число")
        return

    for task in tasks:
        if task.id == task_id:
            print(f"Поточні дані: '{task.title}' ({task.priority})")
            
            new_title = input("Нова назва (залиш пусто щоб не змінювати): ")
            if new_title:
                task.title = new_title
            
            new_description = input("Новий опис (залиш пусто щоб не змінювати): ")
            if new_description:
                task.description = new_description
            
            print("Обери новий пріоритет (1=low, 2=medium, 3=high, 0=залишити як є):")
            priority_choice = input("Обери: ")
            priority_map = {"1": "low", "2": "medium", "3": "high"}
            if priority_choice in priority_map:
                task.priority = priority_map[priority_choice]
            
            save_tasks(tasks)
            print("✓ Задачу оновлено")
            return

    print("✗ Задачу не знайдено")


def delete_task(tasks):
    """Видалити задачу"""
    try:
        task_id = int(input("Введи ID задачі: "))
    except ValueError:
        print("✗ Це не число")
        return

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("✓ Задачу видалено")
            return

    print("✗ Задачу не знайдено")


def mark_done(tasks):
    """Позначити задачу як виконану"""
    try:
        task_id = int(input("Введи ID задачі: "))
    except ValueError:
        print("✗ Це не число")
        return

    for task in tasks:
        if task.id == task_id:
            task.status = "done"
            save_tasks(tasks)
            print("✓ Задачу виконано")
            return

    print("✗ Задачу не знайдено")


def mark_todo(tasks):
    """Позначити задачу як невиконану"""
    try:
        task_id = int(input("Введи ID задачі: "))
    except ValueError:
        print("✗ Це не число")
        return

    for task in tasks:
        if task.id == task_id:
            task.status = "todo"
            save_tasks(tasks)
            print("✓ Задачу позначено як невиконану")
            return

    print("✗ Задачу не знайдено")


def search_tasks(tasks):
    """Пошук задач за назвою або описом"""
    query = input("Що шукаєш? ").lower()
    
    results = [task for task in tasks 
               if query in task.title.lower() or query in task.description.lower()]
    
    if not results:
        print("✗ Немає результатів пошуку")
        return
    
    print(f"\n📍 Знайдено {len(results)} задач(і):")
    for task in results:
        status_icon = "✓" if task.status == "done" else "○"
        priority_icon = {"low": "↓", "medium": "→", "high": "↑"}.get(task.priority, "→")
        print(f"[{task.id}] {status_icon} {task.title} ({priority_icon} {task.priority})")


def sort_tasks(tasks):
    """Сортувати задачі"""
    priority_order = {"high": 0, "medium": 1, "low": 2}
    status_order = {"todo": 0, "done": 1}
    
    print("Обери як сортувати:")
    print("1. За пріоритетом (high → medium → low)")
    print("2. За статусом (невиконані → виконані)")
    print("3. За пріоритетом + статусом")
    
    choice = input("Обери: ")
    
    if choice == "1":
        tasks.sort(key=lambda t: priority_order.get(t.priority, 1))
        print("✓ Відсортовано за пріоритетом")
    elif choice == "2":
        tasks.sort(key=lambda t: status_order.get(t.status, 0))
        print("✓ Відсортовано за статусом")
    elif choice == "3":
        tasks.sort(key=lambda t: (status_order.get(t.status, 0), priority_order.get(t.priority, 1)))
        print("✓ Відсортовано за статусом та пріоритетом")
    else:
        print("✗ Невірний вибір")
