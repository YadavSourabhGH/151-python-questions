#Prime FActor : Factors of a number which are also prime nos
'''
Exmple : 30
        (Factors of 30 are 1, 2, 3, 5, 6, 10)
        Prime factors are 1, 2, 3, 5   (since 6 and 10 are not prime nos)
'''

def prime_factors(number):
    factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors

num = int(input("Enter a number: "))
print(f"Prime factors of {num} are: {prime_factors(num)}")