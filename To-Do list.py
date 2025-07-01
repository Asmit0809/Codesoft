class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            old_task = self.tasks[index]
            self.tasks[index] = new_task
            print(f'Task "{old_task}" updated to "{new_task}".')
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task}" removed from the list.')
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
