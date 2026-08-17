# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [1, 232, 234 , 6756, 65, 723, 3452, 866]
def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))
 
