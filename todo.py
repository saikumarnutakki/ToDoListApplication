def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'Task "{task}" added!')


def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f'Task "{removed_task}" removed!')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
