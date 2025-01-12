'''
91.	**Bubble Sort**
•	Implement bubble sort to sort a list of integers.
'''
myList = [3, 7, 4, 1, 9, 2, 8, 6, 0, 5]     
for j in range(len(myList) - 1):                # Outer loop to control how many times we pass through the list
    for i in range(0, len(myList) - 1 - j):     # Inner loop to go through the list and compare adjacent elements
        if myList[i] > myList[i + 1]:  
            myList[i], myList[i + 1] = myList[i + 1], myList[i]  
print(myList)

        
        
        

