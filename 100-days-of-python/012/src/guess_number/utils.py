"""
Helper functions.
"""

EASY = 10
HARD = 5


def is_correct_guess(user_guess, secret_number):
    """
    Compare the user_guess to the secret_number 
    and return True if they match, False otherwise.
    """
    if user_guess > secret_number:
        print("Too high.")
    elif user_guess < secret_number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {secret_number}.")
        return True
    return False


def set_difficulty():
    """
    Prompt the user to select the difficulty level 
    and returns EASY or HARD accordingly.
    """
    difficulty = input("Choose a difficulty. [easy/hard] ")
    return EASY if difficulty == "easy" else HARD
