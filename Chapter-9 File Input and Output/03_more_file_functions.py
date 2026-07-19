f = open("Chapter-9 File Input and Output/file.txt")

# lines = f.readlines()
# print(f"{lines},\n\n\nThe type of readlines is: {type(lines)}")

# line1 = f.readline()
# print(f"{line1}The type of readlines is: {type(line1)}")

# line2 = f.readline()
# print(f"{line2}The type of readlines is: {type(line2)}")

# line3 = f.readline()
# print(f"{line3}The type of readlines is: {type(line3)}")

# line4 = f.readline()
# print(f"{line4}The type of readlines is: {type(line4)}")

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()
    
f.close()

