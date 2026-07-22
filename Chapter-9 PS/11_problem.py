# Write a python program to rename a file to “renamed_by_ python.txt

with open("Chapter-9 PS/old.txt") as f:
    content = f.read()
    
    
with open("Chapter-9 PS/renamed_by_python.txt", "w") as f:
    f.write(content)