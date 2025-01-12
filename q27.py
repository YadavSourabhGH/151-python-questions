def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    z=abs(a*b)/(gcd(a,b))
    return z

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(f"The LCM of",x,"and",y,"is:", gcd(x, y))