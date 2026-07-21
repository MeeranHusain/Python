# Write a program to mine a log file and find out whether it contains ‘python’. 

with open("Chapter-9 PS/log.txt") as f:
    content = f.read()

if ("python" in content or "Python" in content):
    print("Yes the Python is present")
else:
    print("Yes the Python is present")