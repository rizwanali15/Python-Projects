Task = []

def add():
    user = input("Enter your task: ")
    Task.append(user)
def view():
        if not Task:
            print("Task not found!")
        else:
                print("Your Tasks:",Task)
def Delete():
    user = input("Enter your task: ")
    if user not in Task:
        print("Task not found!")
    else:
        Task.remove(user)
        print("Your remaining Tasks:",Task)
    
while True:
    print("<---TO DO LIST--->")
    print("1. Add")
    print("2. View")
    print("3. Delete")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
       add()
       print(Task)
    elif choice == 2:
        view()
    elif choice == 3:
        Delete()

    elif choice == 4:
        print("Exit! Thank you...")
        break        
    else:
        print("Invalid!...")
    
    
    

