# Sum of Even and Odd Numbers Separately
n = int(input("Enter a number: "))
if n > 0:
    sum_even = sum(i for i in range(1, n + 1) if i % 2 == 0)
    sum_odd = sum(i for i in range(1, n + 1) if i % 2 != 0)
    print(f"Sum of even numbers from 1 to {n}: {sum_even}")
    print(f"Sum of odd numbers from 1 to {n}: {sum_odd}")
else:
    print("Please enter a positive integer.")
