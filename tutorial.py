# # 73. Copy File
# try:
#     with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
#         dest.write(src.read())
# except FileNotFoundError:
#     print("Source file not found.")

#74. Count Lines in a File
# with open("file.txt", "r") as f:
#     print("Total lines:", len(f.readlines()))

#75. Count Words in a File
# with open("file.txt", "r") as f:
#     print("Total words:", sum(len(line.split()) for line in f)) 

#76. Find Longest Line in a File
# with open("file.txt", "r") as f:
#     print("Longest line:", max(f, key=len).strip())

#77. Search for a Word in a File
# word = input("Enter word to search: ")
# with open("file.txt", "r") as f:
#     lines = [i+1 for i, line in enumerate(f) if word in line]
# print("Found in lines:", lines if lines else "Word not found.")

#78. Append to a File 
# text = input("Enter text to append: ")
# with open("output.txt", "a") as f:
#     f.write(text + "\n")


#79. Remove Blank Lines
# with open("file.txt", "r") as f, open("cleaned.txt", "w") as new:
#     new.writelines(line for line in f if line.strip())


#80. File Statistics
# with open("file.txt", "r") as f:
#     data = f.read()
#     print(f"Characters: {len(data)}, Words: {len(data.split())}, Lines: {len(data.splitlines())}")

#81. Class Rectangle
# class Rectangle:
#     def __init__(self, length, width): self.length, self.width = length, width
#     def area(self): return self.length * self.width
#     def perimeter(self): return 2 * (self.length + self.width)

#82. Class Circle
# class Circle:
#     def __init__(self, radius): self.radius = radius
#     def area(self): return 3.14159 * self.radius**2
#     def circumference(self): return 2 * 3.14159 * self.radius

#83. Class BankAccount 
# class BankAccount:
#     def __init__(self, balance=0): self.balance = balance
#     def deposit(self, amount): self.balance += amount
#     def withdraw(self, amount): 
#         if amount > self.balance: print("Insufficient funds.")
#         else: self.balance -= amount
#     def check_balance(self): return self.balance