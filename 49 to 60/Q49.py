# Set Operations
list1 = input("Enter the first list of numbers (separated by space): ").split()
list2 = input("Enter the second list of numbers (separated by space): ").split()

set1 = set(list1)
set2 = set(list2)

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print("Union:", union)
print("Intersection:", intersection)
print("Difference (set1 - set2):", difference)