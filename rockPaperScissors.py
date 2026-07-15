# Rock Paper Scissors Game

import random

options = ("rock", "paper", "scissors")


print()
print("Welcome to Rock, Paper, Scissors!")
print()
username = input("What is your name?: ").title()
print(f"Nice to meet you, {username.title()}!")
print()
running = True
wins_in_row = 0
loses_in_row = 0
ties_in_row = 0

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input(f"{username}, enter a choice (rock, paper, scissors): ")
        print()

    print(f"{username.title()}: {player}\nComputer: {computer}.")

    print()
    if player == computer:
        print("It's a TIE!")
        ties_in_row += 1
        wins_in_row = 0
        loses_in_row = 0
        print(f"{username.title()} and Computer have {ties_in_row} tie(s) in a row!")
    elif player == "rock" and computer == "scissors":
        print(f"{username.title()} WINS!")
        wins_in_row += 1
        ties_in_row = 0
        loses_in_row = 0
        print(f"{username.title()} has {wins_in_row} win(s) in a row!")
    elif player == "paper" and computer == "rock":
        print(f"{username.title()} WINS!")
        loses_in_row = 0
        ties_in_row = 0
        wins_in_row += 1
        print(f"{username.title()} has {wins_in_row} win(s) in a row!")
    elif player == "scissors" and computer == "paper":
        print(f"{username.title()} WINS!")
        loses_in_row = 0
        ties_in_row = 0
        wins_in_row += 1
        print(f"{username.title()} has {wins_in_row} win(s) in a row!")
    else:
        print(f"{username.title()} LOSES!")
        loses_in_row += 1
        wins_in_row = 0
        ties_in_row = 0
        print(f"{username.title()} has {loses_in_row} loss/es in a row!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False
    else:
        print()

print()
print("Thanks for playing!")
