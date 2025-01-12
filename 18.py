# Reverse a Number (While Loop)
num = int(input("Enter a numbernumber: "))
if num > 0:
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print(f"The reversed number is {reversed_num}")
else:
    print("Please enter a positive integer.")
