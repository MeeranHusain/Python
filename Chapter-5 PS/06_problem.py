# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

friend_fav_lan = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
friend_fav_lan.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
friend_fav_lan.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
friend_fav_lan.update({name : lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
friend_fav_lan.update({name : lang})

print(friend_fav_lan)