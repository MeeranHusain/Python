class Employee:
    # language = "Python"
    # salary = 1200000
    
    def __init__(self, name, salary, language):  # dunder method which is automatically called 
        self.name = name
        self.language = language
        self.salary = salary        
        print("I am creating an object")
   
    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")
    
    @staticmethod       # decorator to mark greet as a static method
    def greet():
        print("Good Morning")


name = input("Enter the Name: ")
language = input("Enter you programming language: ")
salary = input("Enter you current salary: ")

meeran = Employee(name, salary, language)

meeran.greet()
meeran.getInfo()
print(meeran.name, meeran.salary, meeran.language)
