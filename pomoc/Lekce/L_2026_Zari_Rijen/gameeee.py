import random

choises = ["rock", "paper", "scissors"]

player = input("choose rock, paper, or scissors: ").lower()
computer = random.choice(choises)

if player == computer:
    print(f"Its a TIEE! Both chose {player}.")
elif player == "rock" and computer == "scissors":
    print("You WIN! Rock beats Scissors.") or\
    print("Computer LOSES!")
elif player == "paper" and computer == "rock":
    print("You WIN! Paper beats Rock.") or\
    print("Computer LOSES!")
elif player == "scissors" and computer == "paper":
    print("You WIN! Scissors beats Paper.") or\
    print("Computer LOSES!")