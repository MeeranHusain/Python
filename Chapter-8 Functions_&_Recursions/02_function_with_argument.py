'''
-------------------------------------------------------------------------------
There are two types of functions in python: 
 • Built in functions (Already present in python) 
 • User defined functions (Defined by the user)

Examples of built in functions includes len(), print(), range() etc. 
The func1() function we defined is an example of user defined function.
-------------------------------------------------------------------------------

'''

def greet(name, ending):
    if (name == "Pankaj"):
        print(f"Kya haal hai dost {name}\n")
    else:
        print(f"Hello, have a good day {name}, {ending}")
    
    return "ok\n\n"

a = greet("harry", "\nThank you\n" )
print(a)
    
greet("Meeran", "\nThank you\n")
greet("Pankaj", "\nThank you\n")


def get_greeting():     # example of return 
  return "Hello from a function"

message = get_greeting()
print(message)