# Break Statement
for i in range (0,80): 
    print(i)     # this will print 0,1,2 and 3 
    if i==3:
        break 
    
# Continue Statement
for i in range(4): 
    if i == 2:   # if i is 2, the iteration is skipped  
        continue 
    print(i)