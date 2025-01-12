'''
89.	**Property Decorators**
•	Create a class that uses @property to control getting and setting of a private attribute.
'''
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute

    # Getter for 'name'
    @property                           # The @property decorator is used for the getter method - when you want to access a certain method like an attribute
    def name(self):
        return self._name

    # Setter for 'name'
    @name.setter                        # @name.setter is the decorator for the setter method which is used when you want to assign value to a var
    def name(self, value):
        if not value:
            print("Name cannot be empty!")
        else:
            self._name = value

# Usage:
person = Person("Alice")                # Object i.e. person created with name Alice

# Accessing and setting name
print(person.name)  # Output: Alice

person.name = "Bob"    # Changing name to Bob
print(person.name)     # Printing : Bob

person.name=""         # Chaging name to null
print(person.name)     # Printing : Name cannot be empty! - since we gave the if-else condition




# Explanation
'''
In normal conditons we would write the two methods as get_age() and set_age() respectively
and when you want to call you will call person.get_age() or person.set_age()
but here you will call just person.name 

Summary:
When you use person.name, it gets the value (calls the getter).
When you assign person.name = "Bob", it sets the value (calls the setter).
The same method name() is used for both getting and setting, but Python knows whether you are trying to get or set based on the syntax you use:
Getter: person.name
Setter: person.name = "Bob"

The neat thing to remember is that we access the private variable through these methods

'''