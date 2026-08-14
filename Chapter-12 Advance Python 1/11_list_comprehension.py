myList = [1, 2, 5, 9, 8, 5, 3]

# squaredList = []
# for item in myList:
#     squaredList.append(item**2)

# print(squaredList)  


# Using list comprehension to create a new list with squares of the elements
squaredList = [i*i for i in myList]
print(squaredList)  # Output: [1, 4, 25, 81, 64, 25, 9]