# Sometimes we want to run a piece of code when try was successful

try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)
    
else:
    print("I am inside else")