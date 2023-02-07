"""
Entry point to the calculator.
"""

from calculator.art import LOGO
from calculator.operations import OPERATIONS


def main():
    """Start calculator and perform calculations."""

    print(LOGO)

    num1 = float(input("What's the first number: "))
    should_continue = True
    while should_continue:
        print(*OPERATIONS)
        operation = input("Pick an operation: ")

        num2 = float(input("What's the next number: "))

        calculate = OPERATIONS[operation]
        answer = calculate(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        should_continue = (
            input(f"Continue calculating with {answer}? [y/n] ").lower() == "y"
        )

        num1 = answer


if __name__ == "__main__":
    main()
