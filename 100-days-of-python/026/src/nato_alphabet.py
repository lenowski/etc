"""
Reads a CSV file with the NATO phonetic alphabet, prompts the user for a word,
and outputs the corresponding NATO phonetic codes for each letter in the entered word.
"""

import pandas as pd


def main():
    # Read NATO phonetic alphabet mapping from CSV
    df = pd.read_csv("src/assets/nato_phonetic_alphabet.csv")
    nato_alphabet = {raw.letter: raw.code for (index, raw) in df.iterrows()}

    # Prompt user for input
    word = input("Enter a word: ").upper()

    # Generate NATO phonetic codes for each letter in the word
    codes = [nato_alphabet[letter] for letter in word if letter in nato_alphabet]

    # Print the resulting NATO phonetic codes
    print(codes)


if __name__ == "__main__":
    main()
