# This file is to practise random number generation in python

import random

low = 1
high = 100
options = ("rock", "paper", "Scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]

number = random.randint(low, high)
option = random.choice(options)
random.shuffle(cards)

print(cards)


#Guessing game

guesses = 0
n = random.randint(low,high)

while True:
    guess = int(input(f" Enter a number between {low} and {high}: "))
    guesses += 1
    if guess < n:
        print(f"The number guessed {guess} is low")
    elif guess > n:
        print(f"The number guessed {guess} is high")
    else:
        print("The guess is correct")
        print(f" you guessed right in {guesses} guesses ")
        break
