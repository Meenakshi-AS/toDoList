import json
tasks = []

def add_task():
    description = input("Enter task description: ")
    task = {"description": description, "completed": False}
    tasks.append(task)
    print("Task added successfully!!")
    

def view_tasks():
    if len(tasks) == 0:
        print("Great! You have no tasks left.")
        return
    print("Your Tasks:")
    sl_no = 1
    for task in tasks:
        if task["completed"]:
            status = "[x]"
        else:
            status = "[ ]"
        print(str(sl_no) + ". " + status + " " + task["description"])
        sl_no += 1


def complete_task():
    if len(tasks) == 0:
        print("Great! You have no tasks left.")
        return
    try:
        num = int(input("Enter the task number to mark as complete: "))
        if num >= 1 and num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print(f"Please enter a valid task number between 1 and {len(tasks)}.")
    except ValueError:
        print("Invalid task number, try again.")


def delete_task():
    if len(tasks) == 0:
        print("The list is empty!! Add more tasks to continue.")
        return
    try:
        num = int(input("Enter the task number to delete: "))
        if num >= 1 and num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully!")
        else:
            print(f"Please enter a valid task number between 1 and {len(tasks)}.")
    except:
        print("Invalid task number, try again.")


def save_tasks():
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Saving tasks to file...")
        print("Tasks saved successfully to tasks.json")
    except Exception as e:
        print("Error saving tasks:",e)


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            print("Loading tasks from file...")
            print("Tasks loaded successfully from tasks.json")
    except FileNotFoundError:
        print("The task file is not found")



def todo():
    print()
    print("Welcome to Task Manager!")
    print()
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            load_tasks()
        elif choice == "7":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    todo()
