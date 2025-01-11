'''
Strong NUmber : A Strong Number is a special number whose sum of the factorials of its digits is equal to the number itself.
Example : 145
        = 1! + 4! + 5!
        = 1 + 24 + 120
        = 145

'''


from math import factorial

def is_strong(number):
    digits = str(number)
    total = 0
    for digit in digits:
        total += factorial(int(digit))
    if total == number:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_strong(num):
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")