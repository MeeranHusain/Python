# A function is a group of statements performing a specific task. 

# When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!

# Function Definition
def avg():
    a = int(input("Enter the number a: "))
    b = int(input("Enter the number b: "))
    c = int(input("Enter the number c: "))
    
    average = (a + b + c) / 3
    print(average)
    
avg() # function call


# Quick Quiz

def greet():
    print("Good Day!")
    
greet()