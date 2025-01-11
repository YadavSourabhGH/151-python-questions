#Convert binary to decimal

def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str) - 1   # (-1) int the end gives the index of the most significant bit (the leftmost bit).
    for digit in binary_str:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

binary = input("Enter a binary number: ")
print(f"The decimal equivalent of {binary} is: {binary_to_decimal(binary)}")