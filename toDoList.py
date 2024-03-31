tasks={}

def addTask():
    task =input("What to do? : ")
    date=input("Date and time ? : ")
    tasks[task] = date


def removeTask(task):
    task=task.lower()
    for item in tasks:
        if task == item.lower():
            tasks.pop(item)
            
    pass

def showList():
    print(tasks)





while True:
    print("Mein menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show to do list")
    
    n=int(input("Enter menu: "))
    match n:
        case 1 :
            addTask()
        case 2:
            removeTask()
        case 3:
            showList()
        case _ :
            print("invalid choice.")
    if n>3 or n<1:
        break

print("Program End\nThank You")