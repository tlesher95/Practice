# Cows and Bulls game :
# Randomly generate a 4-digit number
# Ask the user to guess a 4-digit number
# For every digit that the user guessed correctly in the correct place, they have a “cow”
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have
# Once the user guesses the correct number, the game is over
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end

import random

def goulash(r):
    return number.append(r)

def smash(e):
    return "".join(e)

def ultimate(test):
    x=0
    while x<4:
        test = str(random.randint(0,9))
        goulash(test)
        test = []
        x += 1
    return smash(number)

number = []
# print(f"Random number is: {ultimate(number)}")
ultimate(number)
cows = 0
tries = 0
cowsuffix = "s"
bullsuffix = "s"
while cows != 4:
    cows = 0
    bulls = 0
    tries += 1
    guess = input("Enter your 4 digit guess: ")
    optionsleft = list(number)
    guessesleft = list(guess)
    for z, y in zip(guess, number):
        if z == y:
            cows += 1
            optionsleft.remove(z)
            guessesleft.remove(z)
    for z in guessesleft:
        if z in optionsleft:
            bulls += 1
            optionsleft.remove(z)
    if cows == 1:
        cowsuffix = ""
    if bulls == 1:
        bullsuffix = ""
    if cows == 4:
        print(f"You got it in {tries} tries!")
    else:
        print(f"{cows} cow{cowsuffix}, {bulls} bull{bullsuffix}, keep trying")