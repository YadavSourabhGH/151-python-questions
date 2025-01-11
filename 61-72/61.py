'''ARMSTRONG NUMBER : An Armstrong number is a number where the sum of its digits raised to the power of the number of digits equals the number itself.
# Example: 153
            (number of digits = 3, hence the power of all digits will be 3)
            = 1^3 + 5^3 + 3^3
            = 1 + 125 + 27
            = 153
'''

def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    if total == number:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")