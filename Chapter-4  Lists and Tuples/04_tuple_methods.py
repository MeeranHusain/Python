# There are only 2 methods in tuple:- count and index 

a = (1, 45, 22, False, 22, "Rohan", "Meeran")
print(a)

number = a.count(22)     # checking how many times number are persent into the tuple.
print(number)

i = a.index(45)     # 45 number present at what index, and if not present then give you an error      
print(i)

print(22 in a)      # it check the value is present or not. o/p: True

b = (1,2,5,6)
tupleConcat = a + b     # concated the 2 tuples and created the new tuple without changing the existing tuple.
print(tupleConcat)