# ============== Map Example ==============

l = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, l))
squared = lambda x: x*x
sqList = list(map(squared, l))

print(sqList) 


# ============== Filter Example ==============

def even(x):
    if x % 2 == 0:
        return True
    return False
    
onlyEven = filter(even, l)  # filter take first argument as function and second as iterable object
print(list(onlyEven))


# ============== Reduce Example ==============
# def sum(x, y):
#     return x + y
from functools import reduce
sum = lambda x, y: x + y
mul = lambda x, y: x * y
print(reduce(sum, l))  # reduce take first argument as function and second as iterable object.

print(reduce(mul, l))  # reduce take first argument as function and second as iterable object.


