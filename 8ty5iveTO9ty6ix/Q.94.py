'''
94.	**Merge Sort**
•	Implement merge sort to sort a list of integers.
'''
def merge_sort(arr):
    if len(arr) > 1:                # If the length of the array is greater than 1
        mid = len(arr) // 2         # Find the middle of the array
        L = arr[:mid]               # Divide the array elements into 2 halves - Left Half
        R = arr[mid:]               # Divide the array elements into 2 halves - Right Half
        merge_sort(L)               # Recursively sort the Left Half
        merge_sort(R)               # Recursively sort the Right Half
        i = j = k = 0               # Initialize the index variables
        while i < len(L) and j < len(R):        # Copy data to temp arrays L[] and R[]
            if L[i] < R[j]:                     # Compare the elements of L[] and R[]
                arr[k] = L[i]                   # If L[i] is smaller, copy L[i] to arr[k]
                i += 1                          # Increment the index of L[]
            else:                               
                arr[k] = R[j]                   # If R[j] is smaller, copy R[j] to arr[k]
                j += 1                          # Increment the index of R[]
            k += 1                          # Increment the index of arr[]            
        while i < len(L):           # Check if any element was left
            arr[k] = L[i]           # Copy the remaining elements of L[] to arr[]
            i += 1                  
            k += 1
        while j < len(R):           # Check if any element was left
            arr[k] = R[j]           # Copy the remaining elements of R[] to arr[]
            j += 1
            k += 1
    return arr

arr = [4,8,1,3,5,9,2,6,7]           # Define the array
print(merge_sort(arr))              # Print the sorted array
