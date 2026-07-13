'''
We can have a value as default as default argument in a function. 

If we specify name = “stranger” in the line containing def, this value is used when no argument is passed.

'''

def greet(name, ending = "\nThank you\n\n"):
    print(f"Hello, have a good day {name}, {ending}")
    
greet("Meeran")
greet("Pankaj", "Kya haal ladle\n\n")
greet("Raju")