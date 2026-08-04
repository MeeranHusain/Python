class Number:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):    
        return self.n + num.n
        
n = Number(5)
m = Number(10)

print(n + m)  # This will raise an error because the '+' operator is not defined for Number objects 