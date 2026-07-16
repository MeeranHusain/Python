# Write a python program using function to convert Celsius to Fahrenheit.

def fahrenheit_to_celsius(f):
    return 5*(f-32)/9
    
f = int(input("Enter the temperature in F: "))
c = fahrenheit_to_celsius(f)
# print(f"{c:.2f} °C")
print(f"{round(c, 2)} °C")

