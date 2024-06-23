# To-Do List Application

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Pending"})
        print(f"Task '{task}' added.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['task']} - {task['status']}")
    
    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    
    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["status"] = "Completed"
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")
    
    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task number.")

def menu():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter the task number to complete: "))
            todo_list.complete_task(task_number)
        elif choice == '5':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '6':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    menu()
