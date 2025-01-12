# Count Digits of a Number
num = int(input("Enter a positive integer: "))
if num > 0:
    digit_count = len(str(num))
    print(f"The number of digits in {num} is {digit_count}")
else:
    print("Please enter a positive integer.")
