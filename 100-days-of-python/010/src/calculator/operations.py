"""
Basic arithmetic operations.
"""


def add(n1, n2):
    """Return sum of two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Return difference of two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Return product of two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Return quotient of two numbers."""
    return n1 / n2


OPERATIONS = {
    # fmt: off
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
