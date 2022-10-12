import random

dice = [1, 2, 3, 4, 5, 6]
Computer_roll = random.choice(dice)
User_guess = int(input("Enter number from 1 to 6: "))

if Computer_roll == User_guess:
    print(f"True. Computer rolled {Computer_roll}")
else:
    print(f"False. Computer rolled {Computer_roll}")