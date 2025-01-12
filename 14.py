# Sum of N Natural Numbers
n = int(input("Enter a positive integer: "))
if n > 0:
    total_sum = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is {total_sum}")
else:
    print("Please enter a positive integer.")
