#first way
string = 'You never get a second chance to make a first impression'
print(string.count('e'))


#second way
counter = 0
letter = input("Enter a single letter: ")

for x in string:
    if x == letter:
        counter += 1
    
print(f"Letter {letter} appeared {counter} times. ")

#third way
def func():
    string = input("Enter a string of characters: ")
    counter = 0
    letter = input("Enter a single letter: ")

    for x in string:
        if x == letter:
            counter += 1

    print(f"Letter {letter} appeared {counter} times. ")
    
func()

