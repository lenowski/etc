"""
Contains the MoneyMachine class, which provides functionality for payment processing,
profit tracking, and report generation.
"""


class MoneyMachine:
    """
    Models a payment processor, profit tracker, and report generator.
    """

    CURRENCY = "$"
    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self):
        """
        Initializes a new instance with initial values for profit and money received.
        """
        self.profit = 0
        self.money_received = 0

    def report(self):
        """
        Prints the current profit.
        """
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """
        Prompts the user to insert coins and calculates the total amount of money
        received.
        """
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += (
                int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
            )
        return self.money_received

    def make_payment(self, cost):
        """
        Processes a payment for a given cost.
        """
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        print("Sorry that's not enough money. Money refunded.")
        self.money_received = 0
        return False
