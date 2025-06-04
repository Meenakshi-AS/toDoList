
# Command-Line Task Manager (Python CLI)

## 🎯 Objective
Build a terminal-based To-Do List application where users can:
- Add a task
- View all tasks
- Mark a task as complete
- Delete a task
- Save and load tasks from a file

---

## 🛠️ Features
1. Add Task  
2. View Tasks  
3. Complete Task  
4. Delete Task  
5. Save Tasks  
6. Load Tasks  
7. Exit  

---

## 🧱 Data Structure
Use a list of dictionaries:
```python
tasks = [
    {"description": "Buy milk", "completed": False},
    {"description": "Finish assignment", "completed": True}
]
```

---

## 🔄 Program Flow

### 1. Add Task
- Prompt: `Enter task description`
- Add to list with `completed = False`
- Output: `Task added successfully!`

### 2. View Tasks
- Display all tasks with index, status, and description
- Output: `1. [ ] Task A`

### 3. Complete Task
- Prompt: `Enter task number`
- Set `completed = True`
- Output: `Task marked as complete!`

### 4. Delete Task
- Prompt: `Enter task number`
- Remove task from list
- Output: `Task deleted successfully!`

### 5. Save Tasks
- Save tasks to `tasks.json`
- Output: `Tasks saved successfully!`

### 6. Load Tasks
- Load from `tasks.json`
- Output: `Tasks loaded successfully!`

### 7. Exit
- Output: `Exiting Task Manager. Goodbye!`

---

## 🖥️ Sample Terminal Output
```
Welcome to Task Manager!

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 1

Enter task description: Finish Python assignment
Task added successfully!

--------------------------------------------------

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 1

Enter task description: Submit timesheet
Task added successfully!

--------------------------------------------------

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 2

Your Tasks:
1. [ ] Finish Python assignment
2. [ ] Submit timesheet

--------------------------------------------------

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 3

Enter the task number to mark as complete: 1
Task marked as complete!

--------------------------------------------------

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 2

Your Tasks:
1. [x] Finish Python assignment
2. [ ] Submit timesheet

--------------------------------------------------

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 4

Enter the task number to delete: 2
Task deleted successfully!

--------------------------------------------------

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 5

Saving tasks to file...
Tasks saved successfully to tasks.json

--------------------------------------------------

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 6

Loading tasks from file...
Tasks loaded successfully from tasks.json

--------------------------------------------------

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Save Tasks
6. Load Tasks
7. Exit
Enter your choice: 7

Exiting Task Manager. Goodbye!
```
