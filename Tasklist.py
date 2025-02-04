class TaskList:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def edit_title(self, new_title):
        self.title = new_title

    def get_task(self):
        if not self.tasks:
            return "pup"
        return "\n".join([str(task) for task in self.tasks])

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return (f"Task List: {self.title}\n"
                f"Tasks: {len(self.tasks)}")