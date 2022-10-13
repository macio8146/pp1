PIN = "0805"
number_of_tryes = 0

while(number_of_tryes < 3):
    PIN_ENTERED = str(input("Enter the PIN code: "))
    if(PIN_ENTERED != PIN):
        print("Incorrect...")
        number_of_tryes += 1
    else:
        print("Correct")
        break
else:
    print("Your card has been blocked")
