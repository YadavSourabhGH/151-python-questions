# 108.	**Permutations of a List**

# •	Generate all permutations of a given list of distinct elements.


import itertools

def main():
    lst = [1, 2, 3]
    permutations = list(itertools.permutations(lst))
    print(permutations)

main()  