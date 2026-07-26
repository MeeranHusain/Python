class Employee:
    language = "Python"     # This is a Class Attribute
    salary = 1200000


meeran = Employee()     # Object Instatiation 
meeran.language = "Js"  # Note: Instance attributes, take preference over class attributes during assignment & retrieval.

# --------------- Own Practice --------------- 
# language = input("Write your language: ")
# if language != "":
#     meeran.language = language
#     print(meeran.language, meeran.salary)
# else:
#     print(meeran.language, meeran.salary)
    

meeran.name = "Meeran"  # This is a Instance or Object Attribute
print(meeran.name, meeran.language, meeran.salary)
