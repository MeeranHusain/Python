print("\n====================== Eligible driving age check ======================\n")

age = int(input("Enter your age: "))

# If statement no: 1
if(age%2 == 0):
    print("the number is even")
# End of statement no: 1
    
# If statement no: 2 
if (age > 18):
    print("You can drive")
    
elif(age == 18):
    print(f"Just {age} my boi !!! ")

elif(age <= 0):
    print(f"Enter the valid age, you just entered {age}")    

else:
    print(f"Sorry Boss! grow up, you are just {age}")

# End of statement no: 2
