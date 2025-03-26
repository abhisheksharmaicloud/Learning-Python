# this file is for practising python and trying to build rock paper scissor game

import random

option = ("rock", "paper", "scissor")

running = True

while running:

    player = None
    computer = random.choice(option)

    while player not in  option:
        player = input("enter a choice: ")

    if player == computer:
        print("It is a tie")
    elif player == "rock" and computer == "paper":
        print("the computer wins")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor"and computer == "rock":
        print("The computer wins")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "paper" and computer == "scissor":
        print("Computer wins")
        
    if not input ("play again?").lower() =="y":
        running = False
    print(f"player: {player}")
    print(f"computer: {computer}")