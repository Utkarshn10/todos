import sys 
import os
import json
from colorama import init, Fore

# initializing colorama
init()

def help():
    print(Fore.BLUE + '''
          Use following commands to perform actions:
    \n
    1. List all todos                   python todos.py ls
    2. Add a new todo                   python todos.py add "Todo_Name"
    3. Delete a todo                    python todos.py rm "Todo_Index"
    4. Mark a todo as done              python todos.py done "Todo_Index"
    5. Show all the completed todos     python todos.py ls_done "Todo_Index"
''')
    
def _write_to_todos_file(tasks):
    with open("todos.json","w") as file:
            json.dump(tasks,file,indent=4)
    
def _write_to_done_file(done_task):
    tasks_in_done_list = []
    with open("done.json","r") as file:
        try:
            tasks_in_done_list = json.load(file)
        except:
            pass
    tasks_in_done_list.append(done_task)
    with open("done.json","w") as file:
        json.dump(tasks_in_done_list,file,indent=4)
    
def add(task):
    tasks = []
    task_data = " ".join(map(str,task))

    
    with open("todos.json","r") as file:
        try:
            tasks = json.load(file)
            tasks.append(task_data)
        except: 
            tasks.append(task_data)    

    _write_to_todos_file(tasks)

    print(Fore.GREEN + "Todo added successfully !")

def delete(task_index):
    with open("todos.json","r") as file:
        try:
            tasks = json.load(file)

            del tasks[int(task_index)-1]

            _write_to_todos_file(tasks)
        except:
            print(Fore.RED + "Todo doesn't exist")
    print(Fore.GREEN + "Todo deleted successfully !")

def done(task_index):
    with open("todos.json","r") as file:
        try:
            tasks = json.load(file)

            deleted_task = tasks[int(task_index)-1]

            del tasks[int(task_index)-1]

            _write_to_todos_file(tasks)
            _write_to_done_file(deleted_task)
        except:
            print(Fore.RED + "Todo doesn't exist")
    print(Fore.GREEN + "Todo marked as Done !")
    
def show_done_task_list():
    print("\n")
    print(Fore.BLUE + "Completed Todos")
    print("\n")
    with open("done.json") as file:
        try:
            tasks = json.load(file)
            for index,task in enumerate(tasks):
                displayed_task = str(index+1)+". "+task
                print(Fore.GREEN + displayed_task)
        except:
            print(Fore.RED + "List is Empty !")
    
def show_task_list():
    print("\n")
    print(Fore.BLUE + "Active Todos")
    print("\n")
    with open("todos.json","r") as file:
        try:
            tasks = json.load(file)
            for index,task in enumerate(tasks):
                displayed_task = str(index+1)+". "+task
                print(Fore.GREEN + displayed_task)    
        except:
            print(Fore.RED + "List is Empty !")
            
def update(task_index,updated_task):
    with open("todos.json") as file:
        delete(task_index)
        add(updated_task)
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("Not a valid command.")
        help()
    
    command = args[1]

    '''checking which command is given by the user and performing actions accordingly'''

    if command == 'ls':
        show_task_list()
    
    elif command == 'ls_done':
        show_done_task_list()

    elif command == 'add':
        task = args[2:]
        add(task)

    elif command == 'rm':
        task_index = args[2]
        delete(task_index)

    elif command == 'done':
        task_index = args[2]
        done(task_index)

    elif command == 'update':
        task_index = args[2]
        updated_task = args[3:]
        update(task_index,updated_task)

    elif command == 'help':
        help()
