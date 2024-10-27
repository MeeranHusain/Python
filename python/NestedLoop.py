# WAP of the Nested loop
 
# for i in range(5):
#     for j in range(10):
#         print(i,j)


#WAP to swap the numbers 
# a = 10
# b = 20
# print('Before swap: ', a, b)
# c = a
# a = b
# b = c
# print('After Swap: ', a, b)


# Bubble sort (Brute Force Method)
z = [13, 12, 0 , 3, 7, 17]
for i in range(len(z)):
    for j in range(len(z)):
        if( z[i] < z[j] ):
            z[i], z[j] = z[j], z[i]
            print(z)


# ----This is for the logic to understand the selection sort----
# count = 0
# for i in range(6):
#     for j in range(i+1,6):
#         print(i,j)
#         count=count+1
# count


# Selection sort
# z = [13, 12, 0 , 3, 7, 17]
# print('Before sorting: ',z)
# for i in range(len(z)):
#     k = i
#     for j in range(i+1,len(z)):
#         if z[k] > z[j]:
#             k = j
#     z[i],z[k]=z[k],z[i]
#     print('After Sorting: ',z)
    


# WAP for the prime number
# a = int(input("Enter the range you want to know the list of prime numbers: "))
# for a in range(1,a):
#     count = 0
#     for i in range(1,a+1):
#         if a%i==0:
#             count = count+1
#     if count == 2:
#         print('prime: ', a)
    # else:
    #     print('Not prime: ', a)
    

# Home work is to learn 1) Today's Sorting. , 2) Prime Number / prime number in range from 


# sum = 0
# num = 5
# for i in range(1,num+1):
#     sum = sum+i
#     print(sum)