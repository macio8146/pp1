sum = 0
quantity = 0

while True:
    num = int(input("Enter a number: "))
    if num != 0:
        quantity += 1
        sum += num
    else:
        print(f'Quantity: {quantity}, Sum: {sum}, Mean: {sum/quantity}')
        break
    