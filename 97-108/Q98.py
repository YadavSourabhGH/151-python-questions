# 98.	**Knuth Shuffle (Fisher–Yates Shuffle)**

# •	Given a list, shuffle its elements in place uniformly.

import random

def knuth_shuffle(arr):
    n = len(arr)
    for i in range(n):
        j = random.randint(i, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

# Test the function
arr = [1, 2, 3, 4, 5]
knuth_shuffle(arr)
print(arr)  # Output: Random shuffle of the input list
