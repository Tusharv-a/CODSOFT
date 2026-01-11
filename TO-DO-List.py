class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num - 1)
                print(f"Task '{removed}' deleted.")
            else:
                print("Invalid task number.")

    def menu(self):
        while True:
            print("\n--- TO-DO LIST MENU ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Exit")

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.delete_task()
            elif choice == 4:
                print("Exiting To-Do List. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


todo = TodoList()
todo.menu()
