from task import Task
tasks = []

while True:
    user_input = input("What would you like to do?\ntype help for list of commands: ").lower()

    if user_input == "help":
        print("\nList of Commands\n"
              "-----------------\n"
              "add: Adds new task to task list\n"
              "update: Updates a task in the list\n"
              "delete: Deletes a task from the list\n"
              "mark-in-progress: Marks a task as in progress\n"
              "mark-done: marks a task as done\n"
              "list: lists all tasks\n"
              "list done: lists completed tasks\n"
              "list todo: lists tasks marked as to-do\n"
              "list in-progress: lists tasks marked as in-progress\n")
    elif user_input == "add":
        tasks.append(Task(input("Enter task description: ")))
        
    #elif user_input == "update":
        
    elif user_input == "delete":
        tasks.remove(int(input("Which task would you like to remove 1-" + str(len(tasks) + ": "))) - 1)

        
    #elif user_input == "mark-in-progress":

        
    #elif user_input == "mark-done":
        
    #elif user_input == "list":
        
    #elif user_input == "list done":
        
    #elif user_input == "list todo":
        
    #elif user_input == "list in-progress":
        
    else:
        print("Error Unknown Command")
        