# Multiplication Table
num = int(input("Enter a positive integer: "))
print(f"Multiplication Table for {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
