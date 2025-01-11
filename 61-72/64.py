#SUm of Digits

def sum_of_digits(number):
    total = 0
    for digit in str(number):  #used constructor for iteration
        total += int(digit)    #used constructor for iteration
    return total

num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is: {sum_of_digits(num)}")