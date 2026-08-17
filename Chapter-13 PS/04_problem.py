# 4. Write a program to filter a list of numbers which are divisible by 5. 

def divisible(n):
    if (n%5 == 0):
        return True
    return False
    
a = [1, 23234, 2345346, 675685, 65, 72394, 34532, 865689]
f = list(filter(divisible, a))

print(f)