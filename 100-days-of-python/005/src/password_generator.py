import string
from random import choice, shuffle

LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    password_list = [choice(LETTERS) for _ in range(0, nr_letters)]
    password_list += [choice(NUMBERS) for _ in range(0, nr_numbers)]
    password_list += [choice(SYMBOLS) for _ in range(0, nr_symbols)]
    shuffle(password_list)

    password = "".join(char for char in password_list)

    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()
