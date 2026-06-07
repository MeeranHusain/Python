# WAP to print Number is Palindrome or not 
# content = int(input("Enter the number: "))
# a = content
# b = a 
# c = 0
# while b>0 or b!=0:
#     c= c*10+(b%10)
#     b = b//10
# if c==a:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# WAP to print String is Palindrome or not 
# content = input('Enter the value: ')
# a = content
# b = ''
# for i in a:
#     b = i + b
# if b==a:
#     print("Palindrome")
# else:
#     print('Not palindrome')
    
    

# WAP to print as per the index of (string or number) is Palindrome or not 
# content = input('Enter the value: ')
# a = content
# b = ''
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b==a:
#     print("Palindrome")
# else:
#     print('Not palindrome')
    

# WAP of palindrome using urinary operator
content = input('Enter the value: ')
a = content
p ='is' if a==a[::-1] else 'is not'
print('given string', p, 'palindrome')