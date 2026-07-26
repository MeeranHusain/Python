class Employee:
    language = "Python"
    salary = 1200000
    
    # def __init__(self, language, salary):
    #      self.language = language
    #      self.salary = salary
   
    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")
        
    def greet(self):
        print("Good Morning")

# language = input("Enter you programming language: ")
# salary = input("Enter you current salary: ")
# meeran = Employee(language, salary)

meeran = Employee()     # Object Instatiation 

meeran.greet()
# These both the works same but there is syntacticle difference
meeran.getInfo()
# Employee.getInfo(meeran)
