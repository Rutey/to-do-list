class Category:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def edit_title(self, new_title):
        self.title = new_title

    def __str__(self):
        return (f"Category: {self.title}\n"
                f"Task lists: {len(self.tasks)}")