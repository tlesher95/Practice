# Cows and Bulls game :
# Randomly generate a 4-digit number
# Ask the user to guess a 4-digit number
# For every digit that the user guessed correctly in the correct place, they have a “cow”
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have
# Once the user guesses the correct number, the game is over
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end

import random

num = list(str(random.randint(1000,9999)))
print(num)

def cow_count(x):
    print("Cows: %s" % x)

#FIX BOTH FUNCTIONS

def bull_count(x):
    print("Bulls: %s" % x)


cows = 0
bulls = 0

RUNNING = True
while RUNNING:
    guess = list(str(input("Enter a 4 digit number guess:")))
    if num == guess:
        print("You win!")
        RUNNING = False
    for digit in guess:
        if  guess[0] != num[0]:
            cows = cows + 1
            cow_count(cows)
            bull_count(bulls)
            cows = 0
            bulls = 0
        elif digit != digit in num:
            print("wrong")
    
