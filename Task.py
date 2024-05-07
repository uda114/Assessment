from colorama import init, Fore, Style
from tabulate import tabulate

init()

class TaskWork:
    def __init__(self, title, priority, category, due_date):
        self.title = title
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.completed = False
  