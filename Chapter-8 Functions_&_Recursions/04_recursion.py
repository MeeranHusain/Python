'''
Recursion is a function which calls itself. 
It is used to directly use a mathematical formula as function

'''


def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"The factorial of {n} is {factorial(n)}")
