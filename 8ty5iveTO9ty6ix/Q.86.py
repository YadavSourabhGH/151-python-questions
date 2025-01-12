'''
86.	**Class** ComplexNumber
•	Implement a class that represents a complex number with real and imaginary parts. 
    Overload addition and subtraction operators (if you want to practice operator overloading in Python).
'''
class complex:
    def __init__(self,real,imag):
        self.realPart= real
        self.imaginaryPart = imag
    def __add__(self,number2):                  # Operator Overloading to add two objects
        addition =f"{self.realPart + number2.realPart} + {self.imaginaryPart + number2.imaginaryPart}i"     #Adding real and imaginary parts of number1 and number2
        return addition
    def __sub__(self,number2):                  # Operator Overloading to subtract two objects
        subtraction =f"{self.realPart - number2.realPart} + {self.imaginaryPart - number2.imaginaryPart}i"  #Subtracting real and imaginary parts of number1 and number2
        return subtraction

number1 = complex(5,3)          # Defined object--> number1
number2 = complex(3,2)          # Defined object--> number2

print(number1 + number2)        # call the add function--> overloaded operator to add two objects
print(number1 - number2)        # call the sub function--> overloaded operator to subtract two objects

        