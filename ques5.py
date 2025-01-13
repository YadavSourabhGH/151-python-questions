# Prompt the user for two variables
a = input("Enter the first variable (a): ")
b = input("Enter the second variable (b): ")

# Display values before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swap the values
a, b = b, a

# Display values after swapping
print(f"After swapping: a = {a}, b = {b}")
