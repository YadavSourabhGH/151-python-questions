# sieve_of_eratosthenes : algorithm used to find all prime numbers up to a specified integer n

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # Assume all numbers are prime initially
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, n + 1):  # Check numbers from 2 to n
        if primes[i]:  # If i is prime
            # Mark all multiples of i as not prime
            for j in range(i * 2, n + 1, i):
                primes[j] = False

    # Collect and return all numbers that are still marked as prime
    return [i for i in range(2, n + 1) if primes[i]]

# Get input from the user
n = int(input("Find all primes up to: "))

# Display the result
print(f"Prime numbers up to {n}: {sieve_of_eratosthenes(n)}")