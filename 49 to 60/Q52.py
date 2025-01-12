# Palindrome String Checker
user_string = input("Enter a string: ")

if user_string == user_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")