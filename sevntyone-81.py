# 71. Write to File
# user_input = input("Enter a string to write to the file: ")
# with open("output.txt", "w") as file:
#     file.write(user_input)
# print("String written to output.txt")

#72.read from file
# with open("output.txt","r") as file:
#     data=file.read()
#     print(f"Data read from file: {data}")


# 73. Copy File
# import shutil
# source_file="output.txt"
# destination_file="destination.txt"
# shutil.copy(source_file,destination_file)
# print(f"File copied from {source_file} to {destination_file}")

#74.count lines in a file
# with open("file.txt","r") as f:
#     t_l=len(f.readlines())

#     print("Total lines:",t_l)

#count words in a file
# 75. Count Words in a File
# with open("output.txt", "r") as file:
#     content = file.read()
#     word_count = len(content.split())
# print(f"The file contains {word_count} words.")

# 76. Find Longest Line in a File
# with open("output.txt","r") as f:
#     longest_line=max(f,key=len)
#     print("Longest line in the file is:")
#     print(longest_line)


#77.search for a word in a file
# word=input("Enter word to search: ")
# with open("output.txt","r") as f:
#     lines=[i+1 for i,line in enumerate(f) if word in line] #enumerate function returns the index and the line
# print("Found in lines:",lines if lines else "Word not found.")


#78.append to a file
# text=input("Enter text to append: ")
# with open("output.txt","a") as f:
#     f.write(text + "\n")
#     print("Text appended to file.")

#79.remove blank lines
# with open("output.txt","r") as f,open("cleaned.txt","w") as new:
#     new.writelines(line for line in f if line.strip())
#     print("Blank lines removed.")

#80.file statistics
# with open("output.txt","r") as f:
#     data=f.read()
#     print(f"Characters: {len(data)}, Words: {len(data.split())}, Lines: {len(data.splitlines())}")

# 81. Create a Class Rectangle
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# # Example usage
# rect = Rectangle(5, 3)
# print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")


# 82. Class Circle
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def circumference(self):
#         return 2 * math.pi * self.radius

# # Example usage
# circle = Circle(4)
# print(f"Area: {circle.area()}, Circumference: {circle.circumference()}")

# 83. Class BankAccount
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}, New Balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew: {amount}, New Balance: {self.balance}")

#     def check_balance(self):
#         print(f"Current Balance: {self.balance}")

# # Example usage
# account = BankAccount(100)
# account.deposit(50)
# account.withdraw(30)
# account.check_balance()
