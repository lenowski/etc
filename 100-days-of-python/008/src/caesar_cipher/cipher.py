from string import ascii_lowercase

ALPHABET = ascii_lowercase


def cipher(plain_text, shift, direction):
    alphabet_len = len(ALPHABET)
    if direction == "decode":
        shift *= -1
    ciphered_text = "".join(
        ALPHABET[(ALPHABET.index(char) + shift) % alphabet_len]
        if char in ALPHABET
        else char
        for char in plain_text
    )
    print(f"Here's the {direction}d result: {ciphered_text}")
