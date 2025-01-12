'''
95.	**Quick Sort**
•	Implement quick sort to sort a list of integers.
'''
def quick_sort(arr):
    if len(arr) <= 1:                       # If the length of the array is less than or equal to 1
        return arr                          # Return the array
    else:                                   # Otherwise
        pivot = arr[-1]                     # Define the pivot element
        less = [i for i in arr[:-1] if i < pivot]     # Define the elements less than the pivot
        print(less)
        greater = [i for i in arr[:-1] if i >= pivot] # Define the elements greater than or equal to the pivot
        print(greater)
        return quick_sort(less) + [pivot] + quick_sort(greater)   # Return the sorted array
arr = [4,8,1,3,5,9,2,6,7]           # Define the array
print(quick_sort(arr))              # Print the sorted array