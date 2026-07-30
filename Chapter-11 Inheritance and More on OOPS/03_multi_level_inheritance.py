class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3
    
    
o = Employee()
print(o.a)      # prints the a attribute 
print(o.b)      # shows an error as there is no b attribute in Employee Class 

p = Programmer()
print(p.a)      # prints the a attribute 
print(p.b)      # prints the b attribute 

m = Manager()
print(m.a)
print(m.b)
print(m.c)