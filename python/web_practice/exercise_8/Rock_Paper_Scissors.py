import sys

player1 = input("Enter Player 1's name:")
player2 = input("Enter Player 2's name:")
player1_answer = input("%s, choose either rock, paper, or scissors:" % player1)
player2_answer = input("%s, choose either rock, paper, or scissors:" % player2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == "rock":
        if u2 == "scissors":
            return("%s Wins!" % player1)
        elif u2 == "paper":
            return("%s Wins!" % player2)
        else:
            return("Invalid input, idiot! Must enter either rock, paper, or scissors. Try again.")
    elif u1 == "scissors":
        if u2 == "paper": 
            return("%s Wins!" % player1)
        elif u2 == "rock":
            return("%s Wins!" % player2)
        else:
            return("Invalid input, idiot! Must enter either rock, paper, or scissors. Try again.")
    elif u1 == "paper":
        if u2 == "rock":
            return("%s Wins!" % player1)
        elif u2 == "scissors":
            return("%s Wins!" % player2)
        else:
            return("Invalid input, idiot! Must enter either rock, paper, or scissors. Try again.")
    else:
        return("Invalid input, idiot! Must enter either rock, paper, or scissors. Try again.")
        sys.exit()

print(compare(player1_answer, player2_answer))