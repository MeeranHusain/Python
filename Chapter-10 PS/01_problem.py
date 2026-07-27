# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        

name = input("Enter your Name: ")
salary = input("Enter your Salary: ")
pin = input("Enter your pin-code: ")

meeran = Programmer(name, salary, pin)
print(meeran.name, meeran.salary, meeran.pin, meeran.company)