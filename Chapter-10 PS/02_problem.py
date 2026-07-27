# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, num):
        self.num = num
        
    def square(self):
        square = self.num * self.num
        print(f"square of this {self.num} number is {square:.2f} ")
    
    def cube(self):
        cube = self.num * self.num * self.num
        print(f"cube of this {self.num} number is {cube:.2f} ")
    
    def square_root(self):
        square_root = self.num ** (1/2)
        print(f"square root of this {self.num} number is {square_root:.2f} ")
        

num = int(input("Enter the number: "))
a = Calculator(num)
print("\n1. Square")
print("2. Cube")
print("3. Square Root")

choice = int(input("Enter your choice: "))

if choice == 1:
    a.square()

elif choice == 2:
    a.cube()
    
elif choice == 3:
    a.square_root()

else:
    print("Invalid Choice")
    