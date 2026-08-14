# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’. 

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    
    print(f"the division of a/b is {a/b:.2f} ")

except ZeroDivisionError as Zero:
    print("Infinite")
    
