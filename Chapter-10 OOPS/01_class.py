class Employee:
    language = "Python"     # This is a Class Attribute
    salary = 1200000
    

meeran = Employee()     # Object Instatiation 
meeran.name = "Meeran"  # This is a Instance or Object Attribute
print(meeran.name, meeran.language, meeran.salary)


harry = Employee()      # Object Instatiation
harry.name = "harry"    # This is a Instance or Object Attribute
print(harry.name, harry.language, harry.salary)


# here name is Object Attribute and salary and language is Class Attribute as they directly belongs to the class 
