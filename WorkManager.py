from colorama import init, Fore, Style
from tabulate import tabulate
from Task import TaskWork

init()

class WorkManager:
    def __init__(self):
        self.tasks = []
        
    def addTask(self, title, priority, category, due_date):
        # if priority == 1: priority == "High"
        # elif priority == 2: priority == "Medium"
        # elif priority == 3: priority == "Low"
        
        newTask = TaskWork(title, priority, category, due_date)
        self.tasks.append(newTask)
        
    def viewTask(self):
        tabledata = []
        for i, task in enumerate(self.tasks, start=1):
            # print("Task ID\tPrioroty\tName\t\t\t Category\t Date\t Status")
            # print(f"{i}.\tv{task.priority}\t\t{task.title}\t{task.category}\t{task.due_date}\t{'Completed' if task.completed else 'Pending'}")
            
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))
     
    def priorotyFilter(self, priority):
        filterPriority = []
        tabledata = []
        for task in self.tasks:
            if task.priority == priority:
                filterPriority.append(task)
               
        for i, task in enumerate(filterPriority, start=1):
            # print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))
            
    def CategoryFilter(self, category):
        categoryFilter = []
        tabledata = []
        for task in self.tasks:
            if task.category == category:
                categoryFilter.append(task)
                
        for i, task in enumerate(categoryFilter, start=1):
            #print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))
            
    def DateFilter(self):
        
        tabledata = []
        sortDateTask = sorted(self.tasks, key=lambda x: x.due_date )
        for i, task in enumerate(sortDateTask, start=1):
            #print(f"{i}. [{task.priority}] {task.title} - {task.category} - Due {task.due_date} - {'Completed' if task.comleted else 'Pending'}")
            tabledata.append([i, task.title, task.priority, task.category, task.due_date.strftime("%Y-%m-%d"), 'Completed' if task.completed else 'Pending'])
        headers = ["Index", "Title", "Priority", "Category", "Due Date", "Status"]
        print(tabulate(tabledata, headers=headers, tablefmt="grid"))

    def markComplete(self, index_number):
        try:
            task = self.tasks[int(index_number) - 1]
            task.completed = True
            print(Fore.GREEN + f"Task '{task.title}' is completed!" +Style.RESET_ALL)
        except:
            print(Fore.RED +"Enter a valid task ID"+ Style.RESET_ALL)
            print("\n" +Fore.RED +"Type " +Fore.GREEN +"'help'"+ Style.RESET_ALL+" to see available commands.")
        
    def deleteTask(self, index_number):
        try:
            del self.tasks[int(index_number) - 1]
            print(Fore.GREEN + "Task removed successfully." +Style.RESET_ALL)
        except:
            print(Fore.RED +"Enter a valid task ID"+Style.RESET_ALL)
            print("\n" +Fore.RED +"Type " +Fore.GREEN +"'help'"+ Style.RESET_ALL+" to see available commands.")
