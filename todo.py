tasks = []  
def add_task(task):
    tasks.append(task)
    print(f"task is added : {task}")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("list of tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"task is deleted: {removed}")
    else:
        print("the number of task isn't correct! ")
                                                             
while True:
    print("\n?choose:")
    print("1. Add a task")
    print("2. show tasks")
    print("3. delete a task")
    print("4.Exit")

    choice = input("Enter a number: ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_number = int(input("Enter the number of task to delete: "))
        delete_task(task_number)
    elif choice == "4":
        print("See yeh!")
        break
    else:
        print("Wrong choice. Try again.")