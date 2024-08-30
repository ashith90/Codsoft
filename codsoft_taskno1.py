def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Mark Item as Done")
    print("5. Exit")

def view_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, (task, status) in enumerate(todo_list):
            status_str = "Done" if status else "Not Done"
            print(f"{index + 1}. {task} [{status_str}]")

def add_item(todo_list):
    task = input("\nEnter the task: ")
    todo_list.append((task, False))
    print(f"'{task}' has been added to your list.")

def remove_item(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            item_index = int(input("\nEnter the task number to remove: ")) - 1
            if 0 <= item_index < len(todo_list):
                removed_item = todo_list.pop(item_index)
                print(f"'{removed_item[0]}' has been removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_done(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            item_index = int(input("\nEnter the task number to mark as done: ")) - 1
            if 0 <= item_index < len(todo_list):
                task, _ = todo_list[item_index]
                todo_list[item_index] = (task, True)
                print(f"'{task}' has been marked as done.")
   else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            view_list(todo_list)
        elif choice == "2":
            add_item(todo_list)
        elif choice == "3":
            remove_item(todo_list)
        elif choice == "4":
            mark_done(todo_list)
        elif choice == "5":
            print("\nExiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
