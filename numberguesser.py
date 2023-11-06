import random
number_g = 300
play = 1
cho1 = "a"
cho2 = "a"
print("Welcome to the number guesser!")
while play == 1:
    while number_g > 10 or number_g < 0:
        number_g = int(input("Pick a number between 0 and 10: "))
    number_pc = random.randint(0,10)
    if number_pc == number_g:
        print("You guessed right!")
        while cho1 != "yes" and cho1 != "no":
            cho1 = input("Do you want to play again?(yes/no): ").lower()
        if cho1 == "yes":
            cho1 = "g"
            continue
        else:
            break
    else:
        print("You picked the wrong number:")

    while cho2 != "yes" and cho2 != "no":
        cho2 = input("Do you want to keep going?(yes/no): ").lower()
    if cho2 == "yes":
        number_g = int(input("Pick a number between 0 and 10: "))
        cho2 = "g"
print("Thanks for playing!")