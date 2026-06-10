# Write a python program to display a user entered name followed by Good Afternoon using input () function.
user = input("Enter your name: ")

print("Good Afternoon", user)           # old way
print("Good Afternoon " + user)         # old way concatination
print(f"Good Afternoon {user}")         # f string method