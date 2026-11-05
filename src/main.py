from task_manager import TaskManager


manager = TaskManager()

while True:

    print("\n===== TASK MANAGEMENT SYSTEM =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_id = int(input("Enter Task ID: "))
        title = input("Enter Task Name: ")

        manager.add_task(task_id, title)

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        task_id = int(input("Enter Task ID: "))
        manager.search_task(task_id)

    elif choice == "4":
        task_id = int(input("Enter Task ID: "))
        manager.complete_task(task_id)

    elif choice == "5":
        task_id = int(input("Enter Task ID: "))
        manager.delete_task(task_id)

    elif choice == "6":
        print("Thank you for using Task Management System!")
        break

    else:
        print("Invalid choice. Please try again.")