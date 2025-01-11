'''PERFECT NUMBER : A Perfect Number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
Example : • 6                                    • 28
        (proper divisors - 1,2,3)                 (proper divisors : 1,2,4,7,14)
        = 1 + 2 + 3                                = 1 + 2 + 4 + 7 + 14
        = 6                                        = 28


'''


def is_perfect(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    if total == number:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a Perfect number.")
else:
    print(f"{num} is not a Perfect number.")