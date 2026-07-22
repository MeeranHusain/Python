# Write a program to find out the line number where python is present from ques 6.

with open("Chapter-9 PS/log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line or "Python" in line):
        print(f"Yes the Python is present at this line no: {lineNo}")
        break
    lineNo += 1

else:
    print("NO the Python is Not present")
        