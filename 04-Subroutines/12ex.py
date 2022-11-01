def sum(N):
    if N < 1:
        return N
    else:
        return N + sum(N-1)
    

    

x = 10
print(f'{x} sum = {sum(x)}')
