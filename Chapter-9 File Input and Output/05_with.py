# f = open("Chapter-9 File Input and Output/file.txt")
# print(f.read())
# f.close()


# The same can be written using "with" statement like this:-
with open("Chapter-9 File Input and Output/file.txt") as f:
    print(f.read()) 
    
# you dont have to explicitly close the file.