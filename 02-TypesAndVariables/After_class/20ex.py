import random

dice = [1, 2, 3, 4, 5, 6]
first_choice = random.choice(dice)
second_choice = random.choice(dice)
third_choice = random.choice(dice)

print(f'Fristchoice: {first_choice}')
print(second_choice)
print(third_choice)

sum_of_all_choices = first_choice + second_choice + third_choice
print(sum_of_all_choices)