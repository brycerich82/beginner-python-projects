# Number Guessing Game

import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print()
print("Python Number Guessing game!")
print()
print(f"Select a number between {low} and {high}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print()
            print("That number is out of the given range.")
            print(f"Please select a number between {low} and {high}")
            print()
        elif guess < answer:
            print()
            print("Too low! Try again!")
            print()
        elif guess > answer:
            print()
            print("Too high! Try again!")
            print()
        else:
            print()
            print(f"CORRECT! The answer was {answer}!")
            print(f"You got the answer in {guesses} tries!")
            is_running = False

    else:
        print()
        print("That is not a valid guess.")
        print(f"Please select a number between {low} and {high}")
        print()
