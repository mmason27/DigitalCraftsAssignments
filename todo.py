tasks = {}
while True:
    choice = input("Press 1 to add task, press 2 to delete tasks, press 3 to view all tasks, press q to quit: ")
    if choice == "1":
        title = input("Enter your task: ")
        priority = input("Enter the priority (high/medium/low): ")
        tasks[title] = priority
        # this print statement is only for me to debug my code
        print(tasks)

    # to delete a task
    elif choice == "2":
        print("The following tasks are in your to-do list:")
        for index, (key, value) in enumerate(tasks.items()):
            print (index + 1, key, value)
        delete_task = int(input("Enter the task that you would like to delete from your to-do list: "))
        task = delete_task - 1
        task_to_delete = list(tasks)[task]
        del tasks[task_to_delete]

    # to view all tasks
    elif choice == "3":
        print(f"The following tasks are in your to-do list:")
        for index, (key, value) in enumerate(tasks.items()):
            print (index + 1, key, value)
    elif choice == "q":
        break
    else:
        print("Invalid input, please try again.")


        



