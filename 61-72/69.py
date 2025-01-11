from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_range(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

n = int(input("Enter the range n: "))
print(f"LCM of numbers from 1 to {n} is: {lcm_of_range(n)}")