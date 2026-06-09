#  Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# Specify the directory path
path = "."

# Get the list of files and folders
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")

for item in contents:
    print(item)