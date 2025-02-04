from User import User
from Tasklist import TaskList
from Category import Category
from Task import Task

user1 = User("pipi", "pip3@gmail.com")

input_name = input("Enter name: ")
if user1.check_name(input_name):
    print("Аccess allowed")
    print("Enter 'help' to see other command")
    while True:
        what_do = input("what do: ")
        if what_do == "help":
            print("1. Create new Tasklist\n"
                  "2. Create new Category\n"
                  "3. Create Task\n"
                  "4. Add Task to TaskList\n"
                  "5. Add Tasklist to Category\n"
                  "7. Show Tasklists\n"
                  "8. Show Categories\n"
                  "9. Show Tasks\n"
                  "Exit")

        if what_do == "1":
            num_task_lists = int(input("How many Tasklists do you want to create?\n"))
            for i in range(num_task_lists):
                title = input(f"Write a name for your Tasklist {i + 1}: ")
                new_task_list = TaskList(title=title)
                user1.add_task_list(new_task_list)
                add_task = input("Do you want to add any tasks?\n")
                if add_task == "yes":
                    num_tasks = int(input("How many Tasks do you want to create?\n"))
                    for j in range(num_tasks):
                        name = input(f"Write a name for your Task {j + 1}: ")
                        description = input("White a description: ")
                        new_task = Task(name=name, description=description)
                        new_task_list.add_task(new_task)

            print("Created Tasklists:")
            for idx, task_list in enumerate(user1.task_lists):
                print(f"{idx + 1}. {task_list.title}\n"
                      f"Tasks: {len(task_list.tasks)}")

        if what_do == "2":
            num_categories = int(input("How many Categories do you want to create?\n"))
            for i in range(num_categories):
                title = input(f"Write a name for your Category {i + 1}: ")
                new_category = Category(title=title)
                user1.add_category(new_category)
                add_task_list = input(f"Do you want to add any Tasklists to {user1.categories}?\n")
                if add_task_list == "yes":
                    for idx, task_list in enumerate(user1.task_lists):
                        print(f"{idx + 1}. {task_list.title}")

                    selected_indices = input("Enter the numbers of Tasklists you want to add (comma-separated): ")
                    selected_indices = [int(idx.strip()) - 1 for idx in selected_indices.split(",") if idx.strip().isdigit()]

                    added_task_lists = []
                    for idx in selected_indices:
                        selected_task_list = user1.task_lists[idx]
                        new_category.add_task(selected_task_list)
                        added_task_lists.append(selected_task_list.title)

                    if added_task_lists:
                        print(f"Added Tasklists to {new_category.title}: {', '.join(added_task_lists)}")

            print("Created Categories:")
            for idx, category in enumerate(user1.categories):
                print(f"{idx + 1}. {category.title}")
                      #f"Tasklists: {len(added_task_lists)}")

        if what_do == "3":
            num_tasks = int(input("How many Tasks do you want to create?\n"))
            for i in range(num_tasks):
                name = input(f"Write a name for your Task {i + 1}: ")
                description = input(f"Write a description for your Task {i + 1}: ")
                new_task = Task(name=name, description=description)

            print(user1.task_lists)
            add_to_task_list = input("Which Tasklist do you want to add the task to?\n")
            print("i really lazy to do this")

        if what_do == "7":
            print(user1.get_task_list())

        if what_do == "8":
            print(user1.get_category())

        if what_do == "Exit":
            print("Exiting...")
            break

    #task_list1 = TaskList(title="Work")
    #task_list2 = TaskList(title="Harder Work")
    #user1.add_task_list(task_list1)
    #user1.add_task_list(task_list2)
    # print(user1)
    #user1.get_task_list()
    # print(user1)
    #task1 = Task("pip", "pipipupu")
    #task_list1.add_task(task1)
    # print(task_list1)
    #print(user1.get_task_list())
    #print(task_list1.get_task())









