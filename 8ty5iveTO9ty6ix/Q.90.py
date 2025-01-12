'''
90.	**Class** Employee **with Inheritance**
•	Base class Employee (name, ID, salary) and 
    child class Manager (with additional attributes). Override a method in the subclass.
'''
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name        # Employee's name
        self.emp_id = emp_id    # Employee's ID
        self.salary = salary    # Employee's salary

    def show_details(self):     # Show details function 
        return f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department, team_size):
        # Call the parent class's constructor to initialize name, ID, salary
        super().__init__(name, emp_id, salary)
        self.department = department    # Manager's department
        self.team_size = team_size      # Number of people in the manager's team

    # Override the show_details method to include department and team size
    def show_details(self):
        base_details = super().show_details()  # Call the base class method
        return f"{base_details}, Department: {self.department}, Team Size: {self.team_size}"


employee = Employee("Soham", 101, 50000)                 # Base class object
manager = Manager("Yash", 102, 80000, "IT", 10)        # Derived class object

print(employee.show_details())              # Shows details of employee using method from base class

print(manager.show_details())               # Shows details of manager using the overrriden method from derived class

