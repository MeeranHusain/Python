# Write a program to print half pyramid

# for i in range(0,5):
#     print('*'*(i+1))
 
 
# pyramid into the inverted form

# for i in range(5,0,-1):
#     print('*'*i)


for i in range(6):
    for j in range(i+1):
        print(j+1, end=" ")
    print()


# rows = int(input("Enter number of rows: "))
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()