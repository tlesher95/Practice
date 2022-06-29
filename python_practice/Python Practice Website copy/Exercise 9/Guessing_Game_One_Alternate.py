import random

MIN = int(input("Enter a number to be the minimum value: "))
MAX = int(input("Enter a number to be the maximum value: "))
NUM = random.randint(MIN, MAX)
GUESS = None
ATTEMPT = 0
RUNNING = True

print("Time to give it a shot!")

while RUNNING:
    GUESS = input("Make your guess now:")
    if int(GUESS) < NUM:
        print("Too Low, Try Again!")
    elif int(GUESS) > NUM:
        print("Too High, Try Again!")
    elif GUESS.lower() == "exit":
        print("Better luck next time!")
    elif int(GUESS) == NUM:
        print("You got it!")
        if ATTEMPT <= 2:
            print("Impressive! Only %s tries!" % str(ATTEMPT + 1))
        elif ATTEMPT > 2 and ATTEMPT <= 8:
            print("Not bad! Only %s tries!" % str(ATTEMPT + 1))
        else:
            print("Wow, that took a while! %s tries!" % str(ATTEMPT + 1))
        RUNNING = False
    ATTEMPT += 1