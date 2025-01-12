#Given two lists of equal length, create a third list that stores the element-wise sum.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

sum_list = [x + y for x, y in zip(list1, list2)]

print("Sum of elements:", sum_list)