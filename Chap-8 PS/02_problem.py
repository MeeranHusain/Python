# Write a python program using function to convert Celsius to Fahrenheit.

def fahrenheit_to_celsius(f):
    return 5*(f-32)/9
    
f = int(input("Enter the temperature in F: "))
print(f"{fahrenheit_to_celsius(f):.2f} °C")
