'''
93.	**Selection Sort**
•	Implement selection sort to sort a list of integers.
''' 
arr = [64, 25, 12, 22, 11]              # Define the array
for i in range(len(arr)):               # Traverse through all array elements
    min_index = i                       # Find the minimum element in remaining unsorted array
    for j in range(i+1, len(arr)):      # Swap the found minimum element with the first element
        if arr[min_index] > arr[j]:     
            min_index = j               
    arr[i], arr[min_index] = arr[min_index], arr[i]     
print(arr)
