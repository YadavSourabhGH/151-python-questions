import math  # Importing the math module for square root

# Prompt the user for a number
num = float(input("Enter a number: "))

# Calculate square, cube, and square root
square = num ** 2
cube = num ** 3
square_root = math.sqrt(num)

# Display the results
print(f"Square of {num}: {square}")
print(f"Cube of {num}: {cube}")
print(f"Square root of {num}: {square_root}")
