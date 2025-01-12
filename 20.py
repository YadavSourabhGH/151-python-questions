# Palindrome Checker (Integer)
num = int(input("Enter a positive integer: "))
if num > 0:
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if original_num == reversed_num:
        print(f"{original_num} is a palindrome.")
    else:
        print(f"{original_num} is not a palindrome.")
else:
    print("Please enter a positive integer.")
