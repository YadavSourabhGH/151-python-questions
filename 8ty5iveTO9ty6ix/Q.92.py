'''
92.	**Insertion Sort**
•	Implement insertion sort to sort a list of integers.
'''
arr = [12, 11, 13, 5, 6]            # Define the array
for i in range(1, len(arr)):        # Traverse through 1 to len(arr)
    key = arr[i]                    # Define the key
    j = i-1                         # Define the index       
    while j >= 0 and key < arr[j]:  # Traverse through the array
        arr[j+1] = arr[j]           # Swap the elements
        j -= 1                      # Decrement the index     
    arr[j+1] = key                  # Swap the elements   
print(arr)