import random
rand = random.randint(1,9)
chances = 0
print("Lets play a number guessing game")
while chances<5:
    number = int(input("Guess a number between 1 and 9 and enter it "))
    if number==rand:
        print("You Won!!")
        break
    elif number<rand:
        print("Your guess was too low. Guess a number higher than ",number)

    else:
        print("Your guess was too high. Guess a number lower than ",number)

    chances = chances+1

if chances>=5:
    print("You lost the game")