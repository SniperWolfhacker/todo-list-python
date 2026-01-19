def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

def add_task():
    task = input("Enter new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        tasks.pop(task_no - 1)
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted!")
    except:
        print("Invalid input.")

while True:
    print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
