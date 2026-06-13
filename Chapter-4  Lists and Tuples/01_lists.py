# Python list are containers to store a set of values of any data types.

# Note: strings cannot be change thats why "immutable", but Lists can be change thats why "mutable".

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"] 

print(friends[0])

friends[0] = "Grapes"       # unlike Strings Lists are mutable  
print(friends)
print(friends[0])
print(friends[1:4])         # List slicing possible