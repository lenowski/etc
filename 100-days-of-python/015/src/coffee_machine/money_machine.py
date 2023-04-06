"""
Provides a set of functions to handle payment processing, profit tracking,
and report generation.
"""


COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

profit = {"value": 0, "currency": "$"}


def process_coins():
    """
    Prompts the user to insert coins and calculates the total amount of money received.
    """
    print("Please insert coins.")
    money_received = 0
    for coin in COIN_VALUES:
        money_received += int(input(f"How many {coin}?: ")) * COIN_VALUES[coin]
    return money_received


def make_payment(cost):
    """
    Processes a payment for a given cost.
    """
    money_received = process_coins()
    if money_received >= cost:
        change = round(money_received - cost, 2)
        print(f"Here is ${change} in change.")
        profit["value"] += cost
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def report():
    """
    Prints the current profit.
    """
    print(f"Money: {profit['currency']}{profit['value']}")
