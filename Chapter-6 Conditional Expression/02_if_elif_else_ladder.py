print("\n====================== Eligible driving age check ======================\n")

# If elif else ladder statement
age = int(input("Enter your age: "))

if (age > 18):
    print("You can drive")
    
elif(age == 18):
    print(f"Just {age} my boi !!! ")

elif(age <= 0):
    print(f"Enter the valid age, you just entered {age}")    

else:
    print(f"Sorry Boss! grow up, you are just {age}")
