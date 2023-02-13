"""
Entry point to the Higher/Lower game.
"""


import os

from higher_lower.art import LOGO
from higher_lower.game_data import DATA
from higher_lower.utils import (compare_options, get_random_option,
                                print_options)


def main():
    """
    Main function for running the game.
    """ 
    opt_a = get_random_option(DATA)
    opt_b = get_random_option(DATA)

    score = 0
    while True:
        print(LOGO)
        print_options(opt_a, opt_b)

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == "b":
            opt_a, opt_b = opt_b, opt_a

        if compare_options(opt_a, opt_b):
            score += 1
            print(f"You're right! Current score: {score}:")

            opt_b = get_random_option(DATA)
            DATA.append(opt_b)

            os.system("clear")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break


if __name__ == "__main__":
    main()
