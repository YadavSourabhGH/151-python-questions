'''
96.	**Binary Search**
•	Implement binary search on a sorted list to find a given element.
'''
#without function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]      # Define the array
x = int(input("Enter the number to be searched : "))    # Define the element to be searched
beg = 0                                 # Define the lower bound
end = len(arr) - 1                     # Define the upper bound
while beg <= end:                      # While the lower bound is less than or equal to the upper bound
    mid = (beg + end) // 2             # Define the middle element
    if arr[mid] < x:                    # If the middle element is less than the element to be searched
        beg = mid + 1                   # Update the lower bound
    elif arr[mid] > x:                  # If the middle element is greater than the element to be searched
        end = mid - 1                  # Update the upper bound
    else:                               # Otherwise
        print(f"At Position {mid+1}")                      # Print the position of the element
        break                           # Break the loop
else:
    print(-1)                           # Print -1 if the element is not found
