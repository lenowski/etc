from random import choice

from hangman.art import LOGO, STAGES
from hangman.words import WORD_LIST


def main():
    print(LOGO)

    chosen_word = choice(WORD_LIST)

    display = ["_" for _ in chosen_word]

    lives = 6
    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}.")

        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print("You lose.")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(f"{' '.join(display)}")
        print(STAGES[lives])


if __name__ == "__main__":
    main()
