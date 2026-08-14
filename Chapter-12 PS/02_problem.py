# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [1, 2, 3, 4, 5, 6, 7, 8]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(f"The item at index {i+1} is: {item}")
