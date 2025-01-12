# 97.	**Linear Search**

# •	Implement linear search to find an element in a list.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   

# Test the function
arr = [1, 2, 3, 4, 5]
target = 3
print(linear_search(arr, target))  # Output: 2