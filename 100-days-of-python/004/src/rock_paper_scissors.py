from random import randint

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def main():
    hands = [ROCK, PAPER, SCISSORS]

    player = int(
        input(
            "What do you choose?\n"
            "Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
        )
    )
    print(hands[player])

    print("Oponent chose:")
    oponent = randint(0, 2)
    print(hands[oponent])

    if player == oponent:
        print("It's a draw")
    elif (player == 0 and oponent == 2) or (player > oponent):
        print("You won!")
    else:
        print("You lose")


if __name__ == "__main__":
    main()
