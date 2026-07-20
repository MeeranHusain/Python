# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’

# f = open("Chapter-9 PS/poem.txt")
# data = f.read()
# print(data)
# f.close()

with open("Chapter-9 PS/poem.txt", "r") as poem:
    word = poem.read()
    
    if "twinkle" in word.lower():
        print("the word twinkle is present\n")
        print(word)
    else:
        print("Nope...")
    