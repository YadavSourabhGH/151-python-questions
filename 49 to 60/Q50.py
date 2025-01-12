# Set Membership Testing
names_set = {"Alice", "Bob", "Charlie", "Diana"}

name = input("Enter a name to check: ")

if name in names_set:
    print(f"{name} is in the set.")
else:
    print(f"{name} is not in the set.")