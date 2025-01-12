'''
88.	**Classmethod and Staticmethod**
•	Create a class with a regular instance method, 
    a class method, and a static method. Demonstrate their differences.
'''
class ClassMethods:
    count = 0                       # Class-level attribute

    def __init__(self, value):
        self.value = value          # Instance attribute
        ClassMethods.count += 1     # Increment when an object is created

    # Instance method: Works with instance data
    def show_value(self):
        return self.value           # Returns number given when object is defined

    # Class method: Works with class-level data
    @classmethod
    def show_count(cls):
        return cls.count            # Shows the count i.e. number of objects created

    # Static method: Independent of both class and instance
    @staticmethod
    def greet():                    # Object independent method- doesnt do automatic work when obejct is created
        return "Hello, this is a static method!"


# Creating instances
example1 = ClassMethods(10)
example2 = ClassMethods(20)

# Calling the instance method
print(example1.show_value())  # Output: 10
print(example2.show_value())  # Output: 20

# Calling the class method
print(ClassMethods.show_count())  # Output: 2

# Calling the static method
print(ClassMethods.greet())  # Output: Hello, this is a static method!
