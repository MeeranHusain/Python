'''
1 is for snake
-1 is for water
0 is for gun
'''
# ==================== My Code ====================

import random

computer = random.choice([1, -1, 0])
youStr = input("Enter your choice: ")
youDiction = {"s" : 1,"w" : -1,"g" : 0}
reverseDiction = {1 : "Snake", -1 : "Water",  0 : "Gun"}

you = youDiction[youStr.lower()]

# By now we have 2 numbers (variables), you and computer 

print(f"You choose {reverseDiction[you]}\nComputer choose {reverseDiction[computer]}")
 
if( computer == you ):
    print("It's a Draw 🤝")

else:
    
    if((computer - you) == -1 or (computer - you) == 2):
        print("You Lose! 😓")
    else:
        print("You Win ✨")
     
    # if (computer == -1 and you == 1):       
    #     print("You Win ✨")

    # elif (computer == -1 and you == 0):       
    #     print("You Lose! 😓")
        
    # elif (computer == 1 and you == -1):      
    #     print("You Lose! 😓")

    # elif (computer == 1 and you == 0): 
    #     print("You Win ✨")

    # elif (computer == 0 and you == -1):
    #     print("You Win ✨")

    # elif (computer == 0 and you == 1): 
    #     print("You Lose! 😓") 

    # else:
    #     print("Tie")

# ==================== GPT Code ====================

# import random
# computer = random.choice([1, -1, 0])
# youStr = input("Enter your choice (s/w/g): ").lower()
# if youStr not in ["s", "w", "g"]:
#     print("Invalid Choice")
#     exit()

# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
# you = youDict[youStr]

# print(f"You chose: {reverseDict[you]}")
# print(f"Computer chose: {reverseDict[computer]}")

# if computer == you:
#     print("Tie 🤝")

# elif (
#     (computer == -1 and you == 1) or
#     (computer == 1 and you == 0) or
#     (computer == 0 and you == -1)
# ):
#     print("You Win ✨")

# else:
#     print("You Lose 😓")    
    
    