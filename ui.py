def print_tasks(tasks):
    """Вивести всі задачі красиво"""
    if not tasks:
        print("📭 Немає задач")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Статус':<12} {'Пріоритет':<12} {'Назва':<20} {'Опис':<20}")
    print("=" * 70)
    
    for task in tasks:
        status_icon = "✓ done" if task.status == "done" else "○ todo"
        priority_icon = {"low": "↓ low", "medium": "→ medium", "high": "↑ high"}.get(task.priority, "→ medium")
        
        title = (task.title[:17] + "...") if len(task.title) > 20 else task.title
        description = (task.description[:17] + "...") if len(task.description) > 20 else task.description
        
        print(f"{task.id:<5} {status_icon:<12} {priority_icon:<12} {title:<20} {description:<20}")
    
    print("=" * 70 + "\n")


def print_menu():
    """Вивести головне меню"""
    print("\n" + "─" * 40)
    print(" TASK MANAGER")
    print("─" * 40)
    print("1. Показати всі задачі")
    print("2. Додати нову задачу")
    print("3. Редагувати задачу")
    print("4. Позначити як виконану")
    print("5. Позначити як невиконану")
    print("6.Видалити задачу")
    print("7.Пошук задач")
    print("8.Сортувати задачі")
    print("9. Вийти")
    print("─" * 40)
