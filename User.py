class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.task_lists = []
        self.categories = []

    def check_name(self, input_name):
        return input_name == self.name

    def add_task_list(self, task_list):
        self.task_lists.append(task_list)

    def remove_task_list(self, task_list):
        self.task_lists.remove(task_list)

    def get_task_list(self):
        if not self.task_lists:
            return "pup"
        return "\n".join([str(task_list) for task_list in self.task_lists])

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, category):
        self.categories.remove(category)

    def get_category(self):
        if not self.categories:
            return "pup"
        return "\n".join([str(category) for category in self.categories])

    def __str__(self):
        return (f"Personal data:\n"
                f"username: {self.name}\n"
                f"email: {self.email}\n"
                f"task_lists: {len(self.task_lists)}")