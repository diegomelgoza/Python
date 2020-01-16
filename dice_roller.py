import random

while True:
    dice = int(input("What type of dice would you like to roll?\n"))
    print("You rolled a " + str(random.randint(1, dice)))
    response = input("Enter 'Yes' if you would like to roll again.\n")
    if response.lower() == 'yes':
        continue
    else:
        print("Goodbye!")
        break



