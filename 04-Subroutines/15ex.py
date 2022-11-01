import mymath

attempts = 3

while attempts > 0:
    num = mymath.read_number()
    x = mymath.generate_number()

    if num == x:
        print("You won")
        break
    else:
        print("Try again")
        attempts -= 1
else:
    print("You lost")
