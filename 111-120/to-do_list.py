# 10. Todo List - Task manager
class TodoList:
    def __init__(self):
        self.tasks = []  # List to store tasks
    
    def add_task(self, task):
        # Add new task as not completed
        self.tasks.append({"task": task, "completed": False})
        
    def complete_task(self, task_number):
        # Mark task as completed
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            
    def view_tasks(self):
        # Show all tasks and their status
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i+1}. [{status}] {task['task']}")