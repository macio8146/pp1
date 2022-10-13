dogs_age = float(input("Enter dog's age: "))

if dogs_age <= 2:
    print(f"The dog's age in dog's years is {dogs_age * 10.5}")
else:
    print(f"The dog's age in dog's years is {2 * 10.5 + (dogs_age - 2) * 4} years")