# Power Function
def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} to the power of {exponent} is {power(base, exponent)}")
