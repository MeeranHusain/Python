# Inheritance is a way of creating a new class from an existing class.

class Employee:         # This is called Base class or Parent class 
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} ")
        
# class Programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary} ")
        
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):     # This is called Inherited, Derived or Child class
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
    
        
a = Employee()
b = Programmer()

print(a.company, b.company) 