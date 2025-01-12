#Write a function to reverse a given list in place.

def reverse_list(lst):
    lst.reverse()

my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print("Reversed list:", my_list)