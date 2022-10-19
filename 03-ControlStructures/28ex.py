n0 = 0
n1 = 1

for i in range(51):
    x = n0 + n1
    n0 = n1 
    n1 = x
    print(x, end=", ")
    
