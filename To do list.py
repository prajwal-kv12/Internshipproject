class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        print("To-Do List:\n" + '\n'.join(f"{i}. {task}" for i, task in enumerate(self.tasks, start=1)) or "No tasks.")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def delete_task(self, task_index):
        try:
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task}' deleted.")
        except IndexError:
            print("Invalid index. Please enter a valid one.")

def todo_list():
    todolist = ToDoList()

    while True:
        print("\nTo-Do List\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Quit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            todolist.display_tasks()
        elif choice == '2':
            todolist.add_task(input("Enter task to add: "))
        elif choice == '3':
            todolist.display_tasks()
            todolist.delete_task(int(input("Enter index to delete: ")))
        elif choice == '4':
            print("Quitting. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-4.")

if __name__ == "__main__":
    todo_list()

