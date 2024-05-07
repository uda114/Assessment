import datetime
import time
from colorama import init, Fore, Style
from WorkManager import WorkManager

init()

def validatePriority(priority):
    
    # priorities = ["1", "2", "3"]
    priorities = ["High", "Medium", "Low"]
    if priority.capitalize() in priorities:
        return True
    else:
        print(Fore.RED + "Invalid priority. Please enter High, Medium, or Low." +Style.RESET_ALL)
        return False

def validateCatagory(catagory):
    # catagories = ["1", "2"]
    catagories = ["Personal", "Business"]
    if catagory.capitalize() in catagories:
        return True 
    else:
        print(Fore.RED + "Invalid catagory. Please enter Personal, or Business." + Style.RESET_ALL)
        return False

def validateNumber(number):
    if number.isdigit():
        return True
    else:
        print(Fore.RED + "Invalid input. Enter only numbers" + Style.RESET_ALL)
        return False
    
def setPriority(priority):
    
    if priority == "1": 
        priority = "High" 
        return priority
    elif priority == "2": 
        priority = "Medium" 
        return priority
    elif priority == "3": 
        priority = "Low"
        return priority
    
def setCatagory(category):
    if category == "1": 
        category = "Personal" 
        return category
    elif category =="2": 
        category = "Business" 
        return category
        
def validateTitle(title):
    if title == "":
        print(Fore.RED + "Invalid Title. Please enter correct title." +Style.RESET_ALL)
        return False
    else:
        return True
  
def taskInput():
    
    title = input("\nEnter task name: \n > ")
    while not validateTitle(title):
        title = input("\nEnter task name: \n > ")
    
    priority = input("\nEnter task priority (High, Medium, or Low): \n > ")
    
    while not validatePriority(priority):
        priority = input("\nEnter task priority (High, Medium, or Low): \n > ")
    
    # priority = setPriority(priority)
    
    
    category = input("\nEnter task category (Personal, or Business): \n > ")
    
    while not validateCatagory(category):
        category = input("\nEnter task category (Personal, or Business): \n > ")
    
    # category = setCatagory(category)
    
    
    dategiven = input("\nEnter due date (YYYY-MM-DD): \n > ")
    while (True) :
        try: 
            due_date = datetime.datetime.strptime(dategiven, "%Y-%m-%d").date()
            if due_date >= datetime.date.today():
                break
            else:
                dategiven = input("\nEnter a date in "+Fore.RED+"future"+Style.RESET_ALL+" (YYYY-MM-DD): \n > ")
        except: 
            dategiven = input("\nEnter "+Fore.RED+"a valid"+Style.RESET_ALL+" due date (YYYY-MM-DD): \n > ")
        
    
    return title, priority, category, due_date


if __name__ == "__main__":
    
    Work_Manager = WorkManager()
    
    print("====== Welcome to Task Manager CLI! ======")
    print("\n" +Fore.RED +"Type " +Fore.GREEN +"'help'"+ Style.RESET_ALL+" to see available commands.")
    
    while True:
        
        # print("\n" +Fore.RED +"Type " +Fore.GREEN +"'help'"+ Style.RESET_ALL+" to see available commands.")
        choice = input("\n > ")

        if (choice.capitalize() == "Add"):
            title, priority, category, due_date = taskInput()
            Work_Manager.addTask(title, priority, category, due_date)
            print(Fore.GREEN +"\n Task added successfully." + Style.RESET_ALL)
            
        elif (choice.capitalize() == "List"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            
        elif (choice.capitalize() == "Priority"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            priority = input("\nEnter priority to filter by (High, Medium, or Low): ")
            while not validatePriority(priority):
                priority = input("\nEnter task priority High, Medium, or Low: ")
            # priority = setPriority(priority)
            Work_Manager.priorotyFilter(priority)
            
        elif (choice.capitalize() == "Category"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            category = input("\nEnter task category (Personal, or Business): ")
            while not validateCatagory(category):
                category = input("\nEnter task category (Personal, or Business): ")
            # category = setCatagory(category)
            Work_Manager.CategoryFilter(category)
            
        elif (choice.capitalize() == "Date"):
            print("\n\nView All Sorted Tasks:")
            Work_Manager.DateFilter()
            
        elif (choice.capitalize() == "Complete"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            taskNumber = input("\nEnter the index of the task to mark as complete: ")
            while not validateNumber(taskNumber):
                taskNumber = input("\nEnter the index of the task to mark as complete: ")
            Work_Manager.markComplete(taskNumber)
            
        elif (choice.capitalize() == "Delete"):
            print("\n\nView All Tasks:")
            Work_Manager.viewTask()
            delTaskNumber = input("\nEnter the index of the task to remove: ")
            while not validateNumber(delTaskNumber):
                delTaskNumber = input("\nEnter the index of the task to remove: ")
            Work_Manager.deleteTask(delTaskNumber)
        
        elif (choice.capitalize() == "Help"):
            
            print("\nAvailable commands:")
            print("\n -"+Fore.BLUE+" add"+Style.RESET_ALL+": Add a new task")
            print(" -"+Fore.BLUE+" list"+Style.RESET_ALL+": List all tasks")
            print(" -"+Fore.BLUE+" priority"+Style.RESET_ALL+": View taks by priority")
            print(" -"+Fore.BLUE+" category"+Style.RESET_ALL+": View task by category")
            print(" -"+Fore.BLUE+" date"+Style.RESET_ALL+": Sort task by due date")
            print(" -"+Fore.BLUE+" complete"+Style.RESET_ALL+": Mark a task as complete")
            print(" -"+Fore.BLUE+" delete"+Style.RESET_ALL+": Remove a task")
            print(" -"+Fore.BLUE+" exit"+Style.RESET_ALL+": Exit application")
        
        elif (choice.capitalize() == "Exit"):
            print(Fore.RED + "Exiting..." +Style.RESET_ALL)
            print(Fore.RED + "..Thank you for using Task manager.." +Style.RESET_ALL)
            time.sleep(3)
            break
        else:
            print(Fore.RED +"Invalid command. Please try again." + Fore.RESET)
            
    