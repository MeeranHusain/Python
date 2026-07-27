# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?


class Demo:
    a = 4       # This is a Class Attribute
    
o = Demo()      # Object Instatiation 
print(o.a)
o.a = 1         # This is a Instance or Object Attribute 
print(o.a)