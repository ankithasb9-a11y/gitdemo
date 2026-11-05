class Task:

    def __init__(self, task_id, title):
        self.task_id = task_id
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def display(self):
        status = "Completed" if self.completed else "Pending"

        print(f"ID: {self.task_id}")
        print(f"Task: {self.title}")
        print(f"Status: {status}")