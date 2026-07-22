# Write a program to find out whether a file is identical & matches the content of another file

file1 = input("Enter the first file name or path here: ")
file2 = input("Enter the Second file name or path here: ")

# with open("Chapter-9 PS/this.txt") as f:
with open(file1) as f:
    content1 = f.read()
    
# with open("Chapter-9 PS/poem.txt") as f:
with open(file2) as f:
    content2 = f.read()
    
if (content1 == content2):
    print("Yes these files are identical")
else:
    print("No these files are identical")
    
