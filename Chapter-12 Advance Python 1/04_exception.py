try:
    a = int(input("Enter a number: "))
    print(a)
    
except ValueError as val:
    print(f"Hey this is {val}")

except Exception as e:
    print(type(e))
    print(e)

print("Thank you!")