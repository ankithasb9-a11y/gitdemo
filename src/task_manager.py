from task import Task


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, title):
        task = Task(task_id, title)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            task.display()
            print("----------------")

    def search_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.display()
                return

        print("Task not found.")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                print("Task completed successfully!")
                return

        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return

        print("Task not found.")