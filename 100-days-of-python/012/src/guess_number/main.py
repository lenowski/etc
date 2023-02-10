"""
Entry point to the Guess the Number game.
"""

import random

from guess_number.art import LOGO
from guess_number.utils import is_correct_guess, set_difficulty


def main():
    """
    Play the Guess the Number game.
    """
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {secret_number}")
    tries = set_difficulty()

    for i in range(tries):
        guess = int(input("Make a guess: "))

        if is_correct_guess(guess, secret_number):
            break

        if i != tries - 1:
            print(f"You have {tries - i - 1} attempts remaining to guess a number.")
        else:
            print("You've run out of guesses, you lose.")


if __name__ == "__main__":
    main()
