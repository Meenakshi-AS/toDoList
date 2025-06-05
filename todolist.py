import json

class ToDoList:
    def __init__(self):
        self.tasks=[]
        self.load_tasks() 

    def add_task(self):
        description = input("Enter task description: ")
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        print("Task added successfully!!")
        

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("Great! You have no tasks left.")
            return
        print("Your Tasks:")
        sl_no = 1
        for task in self.tasks:
            if task["completed"]:
                status = "[x]"
            else:
                status = "[ ]"
            print(str(sl_no) + ". " + status + " " + task["description"])
            sl_no += 1


    def complete_task(self):
        if len(self.tasks) == 0:
            print("Great! You have no tasks left.")
            return
        try:
            num = int(input("Enter the task number to mark as complete: "))
            if num >= 1 and num <= len(self.tasks):
                self.tasks[num - 1]["completed"] = True
                print("Task marked as complete!")
            else:
                print(f"Please enter a valid task number between 1 and {len(self.tasks)}.")
        except ValueError:
            print("Invalid task number, try again.")


    def delete_task(self):
        if len(self.tasks) == 0:
            print("The list is empty!! Add more tasks to continue.")
            return
        try:
            num = int(input("Enter the task number to delete: "))
            if num >= 1 and num <= len(self.tasks):
                self.tasks.pop(num - 1)
                print("Task deleted successfully!")
            else:
                print(f"Please enter a valid task number between 1 and {len(self.tasks)}.")
        except:
            print("Invalid task number, try again.")


    def save_tasks(self):
        try:
            with open("tasks.json", "w") as file:
                json.dump(self.tasks, file)
            print("Saving tasks to file...")
            print("Tasks saved successfully to tasks.json")
        except Exception as e:
            print("Error saving tasks:",e)


    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
                print("Loading tasks from file...")
                print("Tasks loaded successfully from tasks.json")
        except FileNotFoundError:
            print("The task file is not found")



    def todo(self):
        print("Welcome to Task Manager!")
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
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.save_tasks()
            elif choice == "6":
                self.load_tasks()
            elif choice == "7":
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Please enter a valid choice.")

if __name__ == "__main__":
    todolist=ToDoList()
    todolist.todo()
