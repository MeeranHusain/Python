# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

words = {
    "Madad" :   "Help", 
    "Billi" :   "Cat",
    "Kursi" :   "Chair"
}

word = input("Enter the word you want to know meaning of: ")
print(f"The {word} is called in english is;",words[word])
