
Todo_list = []

while True:
    print('''=====TO DO LIST MENU====='
    1. View To-Do List
    2. Add Task
    3. Edit Task  
    4. Remove Task
    5. Exit''')

    choice = input('\nEnter number: ')

    match choice:
        case '1': #View To-Do List
            if not Todo_list:
                print('Your To-Do List is empty')
            else:
                print('Your To-Do List:')
                for i, task in enumerate(Todo_list, start=1):
                    print(f"{i}.{task}")
                    print()
        case '2': #Add Task
            task = input('\nEnter Task Name: ')
            Todo_list.append(task)
            print('Task Added...')

        case '3': #Edit Task
            if not Todo_list:
                print('\nYour To-Do List is empty, nothing to edit bro...')
            else:
                for i, task in enumerate(Todo_list, start=1):
                    print(f"{i}.{task}")
                try:
                    task_number = int(input('Enter task number: '))
                    if 1 <= task_number <= len(Todo_list):
                        new_task = input('Enter new task: ')
                        Todo_list[task_number] = new_task
                        print('Task Updated')
                    else:
                        print('Invalid task number, Try again')
                except ValueError:
                    print('Please enter a valid number please')

        case '4': #Remove Task
            if not Todo_list:
                print('\nYour To-Do List is empty, Nothing to remove bro...')
            else:
                for i, task in enumerate(Todo_list, start=1):
                    print(f"{i}.{task}")
                try:
                    task_number = int(input('Enter task number to remove: '))
                    if 1 <= task_number <= len(Todo_list):
                        removed = Todo_list.pop(task_number - 1)
                        print(f"Task Removed: {removed}")
                    else:
                        print('Invalid task number')

                except ValueError:
                    print('Please enter a valid number please')

        case '5': #Exit
            print('\nExiting System....')
            break

        case _:
            print('Invalid choice ka bro')


