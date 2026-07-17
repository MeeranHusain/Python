# Write a python function which converts inches to cms. 

def inch_to_cms(n):
    return n * 2.54

n = int(input("Enter the value in inches: "))
print(f"The value in cms is {inch_to_cms(n)}")
    