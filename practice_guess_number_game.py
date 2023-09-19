#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

Easy_level_turns = 10
Hard_level_turns = 5


# function of difficulties
def set_difficulty():
    level = input("type the 'easy'or 'hard'to set difficulty!")
    if level == "easy":
        return Easy_level_turns
    else:
        return Hard_level_turns


# function to check the guess  against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
    else:
        print("you got it right! the answer was {answer}.")


#choosing a random number between 1 to 100
from random import randint

print("Welcome to the Number Guessing Game!")
print("I'm thinking a number between 1 to 100.")
answer = randint(1, 101)
print(f"Pssst, the correct answer is {answer}")

turns = set_difficulty()
print(f"you got {turns} attempts remaining to guess the number")

#users make a guess
guess = int(input("Make a guess:"))

#track the number of turns and reduce by 1 if they get it wrong

#reapet the function until it right
