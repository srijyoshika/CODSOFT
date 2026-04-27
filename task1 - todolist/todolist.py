#to do list
import sys
tasks = []
def add():
    task_name = input("Enter the task to add: ")
    tasks.append({"name": task_name, "status": "Pending"})
    print("added successfully!")

def view():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        print("\n---- CURRENT TASKS ----")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} --> {task['status']}")

def complete():
    view()
    if len(tasks) == 0:
        return
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Completed"
            print("Task completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete():
    view()
    if len(tasks) == 0:
        return
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed['name']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n========== MY TO DO LIST MANAGER ==========")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")
    ch = int(input("Choose an option from (1 to 5): "))
    match ch:
        case 1:
            add()
        case 2:
            view()
        case 3:
            complete()
        case 4:
            delete()
        case 5:
            print("Thank you for using to do list !")
            sys.exit()
        case _:
            print("Invalid choice")
