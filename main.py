from storage import load_tasks
from task_manager import (
    add_task, edit_task, delete_task, mark_done, mark_todo, 
    search_tasks, sort_tasks
)
from ui import print_tasks, print_menu


def main():
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Обери: ").strip()

        if choice == "1":
            print_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            mark_todo(tasks)
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            search_tasks(tasks)
        elif choice == "8":
            sort_tasks(tasks)
        elif choice == "9":
            print("👋 До побачення!")
            break
        else:
            print("✗ Невірний вибір")


if __name__ == "__main__":
    main()