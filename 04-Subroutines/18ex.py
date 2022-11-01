def func(num):
    
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    
    return sum 
    

print(func(7129))