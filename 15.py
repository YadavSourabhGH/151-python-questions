# Factorial of a Number
num = int(input("Enter a non-negative integer: "))
if num >= 0:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
else:
    print("Please enter a non-negative integer.")
