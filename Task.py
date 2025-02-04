class Task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    # еще методы

    def set_reminder(self, reminder):
        self.reminder = reminder

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return (f"name: {self.name}\n"
                f"description: {self.description}")