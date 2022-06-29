import random

num = random.randint(1, 9)
guess = int(input("Guess a number between 1 and 9!"))
def compare(num, guess):
    if guess < num:
        return("Too Low!")
    elif guess > num:
        return("Too High!")
    else:
        return("You got it!")

print(compare(num, guess))