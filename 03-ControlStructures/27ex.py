i = 0
j = 0
l = 6
m = 1

while i < 9:
    print(l + m, end=" ")
    m += 1

    j += 1
    if j % 3 == 0:
        print()
        l = l - 3
        m = 1 
    
    i = i + 1   
