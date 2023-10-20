#Rock, Paper, Scissors
import random

# Variables
user_guess = input("Rock, Paper, or Scissors? ")
computer_guess = random.randint(1, 3)

#Sanatize Input
user_guess = user_guess.upper()

#Generates Computer's Guess
if computer_guess == 1:
    computer_guess = "ROCK"

elif computer_guess == 2:
    computer_guess = "PAPER"

else:
    computer_guess = "SCISSORS"

#Functions
win = lambda : print("You win!")
lose = lambda : print("You lose!")
tie = lambda : print("Tie!")

#State Guesses
print("You picked:", user_guess)
print("The computer picked:", computer_guess)

#Determine Winner
#Rock
if user_guess == "ROCK" and computer_guess == "SCISSORS":
    win()
elif user_guess == "ROCK" and computer_guess == "ROCK":
    tie()
elif user_guess == "ROCK" and computer_guess == "PAPER":
    lose()
#PAPER
elif user_guess == "PAPER" and computer_guess == "ROCK":
    win()
elif user_guess == "PAPER" and computer_guess == "PAPER":
    tie()
elif user_guess == "PAPER" and computer_guess == "SCISSORS":
    lose()
#SCISSORS
elif user_guess == "SCISSORS" and computer_guess == "PAPER":
    win()
elif user_guess == "SCISSORS" and computer_guess == "SCISSORS":
    tie()
elif user_guess == "SCISSORS" and computer_guess == "ROCK":
    lose()
else:
    print("USER GUESS ERROR")

#END OF CODE
