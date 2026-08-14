# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with open("Chapter-12 PS/1.txt", "r") as file1:
        print(file1.read())

except Exception as e:
    print(e)

try:
    with open("Chapter-12 PS/2.txt", "r") as file2:
        print(file2.read())

except Exception as e:
    print(e)

try:
    with open("Chapter-12 PS/3.txt", "r") as file3:
        print(file3.read())

except Exception as e:
    print(e)

print("Thank you")