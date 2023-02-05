import sys

from caesar_cipher.art import LOGO
from caesar_cipher.cipher import cipher


def main():
    print(LOGO)

    should_end = False
    while not should_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))

        cipher(text, shift, direction)

        restart = input("Type 'yes' to go again, type 'no' to quit: ")
        if restart == "no":
            should_end = True
            print("Goodbye")


if __name__ == "__main__":
    sys.exit(main())
