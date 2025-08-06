class Task:
    def __init__(self,description,priority):
        self.description = description  # Task description (e.g., "Buy groceries")
        self.priority = priority        # Task priority (High/Medium/Low)
        self.completed = False          # Task completion status (default: not completed)
    def __str__(self):                  # Return a readable format
        return f"Description: {self.description},\nPriority: {self.priority},\n completed:{'YES' if self.completed else 'NO'}"

class ToDoList:
    def __init__(self):
        self.tasks = []                 # Initialize an empty list to store tasks

    def add_task(self,task):
        self.tasks.append(task)         # Add a new task to the list

    def display_task(self):
        if self.tasks:                  # Display all tasks in the list
            print("Tasks in the To-Do List:")
            for index,task in enumerate (self.tasks, start = 1):
                print(f"{index}. {task}")
        else:
            print("No Tasks in the To-Do List.")

    def mark_task_completed(self,index):  # Mark a task as completed based on its index
        if index>=1 and index<=len(self.tasks):
            task = self.tasks[index-1]
            task.completed = True
            print(f"Task '{task.description}' marked as completed.")
        else:
            print("Invalid Task Index")


todo_list = ToDoList()                     # Create an instance of ToDoList

task1 = Task("Complete Project Report","High")
task2 = Task("Call the Client","Medium")
task3 = Task("Buy Fruits","Low")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

todo_list.display_task()

todo_list.mark_task_completed(1)

todo_list.display_task()
