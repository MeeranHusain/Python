# Write a program using functions to find greatest of three numbers. 

def greatestNumber(a, b, c):
    if (a>b and a>c):
        # print(f"Number {a} is the greatest.")
        return f"{a} is the greatest number"
    elif(b>c and b>a):
        # print(f"Number {b} is the greatest.")
        return f"{b} is the greatest number" 
    else:
        # print(f"Number {c} is the greatest.")
        return f"{c} is the greatest number"

a = int(input("Enter the number of a: "))
b = int(input("Enter the number of b: "))
c = int(input("Enter the number of c: "))

print(greatestNumber(a,b,c))

        