todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def mark_complete(index):
    if 1 <= index <= len(todo_list):
        todo_list[index - 1] = f"✅ {todo_list[index - 1]}"
        print("Task marked as complete.")
    else:
        print("Invalid index.")



while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Complete")
    

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    
