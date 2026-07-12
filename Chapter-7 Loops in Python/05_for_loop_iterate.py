# For loops with List
li = [1, 4, 6, 234, 6, 764]
for i in li:
    print(i)
print(" ===================================================\n")

# For loop with Tuples
tu = (6, 231, 4, 65)
for t in tu:
    print(t)
print(" ===================================================\n")

# For loop with strings
s = "Harry"
for i in s:
    print(i)
print(" ===================================================\n")

# Personal logic practice  
st = "Meeran"
for s in range(len(st)):
    for j in range(s+1):
        print(st[j], end= " ")
    print()