a = 89

def fun():
    global a   # this will tell python that we are using the global variable a
    a = 3       # a is a local variable for this fun()
    print(a)

print(a)   # this will print the global variable a
fun()   
print(a)   # this will print the global variable a because we have used the global keyword in fun() to modify the global variable a