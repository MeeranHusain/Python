# A tuple is an immutable data type in python.

# a = () # empty tuple.
# a = (1,) # tuple with only one element needs a comma.     ✅ 
# a = (1)  # tuple without comma understand as integer type. ❌

a = (1,2,5,6) # tuple with more than one element
print(type(a))
     
b = (1, 45, 22, False, "Rohan", "Meeran")
# b[0] = "Hello"        # shows an error because tuple is immutable same as strings
print(b)
