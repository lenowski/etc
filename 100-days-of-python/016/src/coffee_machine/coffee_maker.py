"""
Contains the CoffeeMaker class, which provides functionalty
for check resources, make coffee, and report generation.
"""


class CoffeeMaker:
    """
    Models the machine that makes the coffee.
    """

    def __init__(self):
        """
        Initializes a new instance with default values for the resources.
        """
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """
        Prints a report of all resources.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Checks if there are enough resources to make a given drink.
        """
        if any(
            [
                self.resources[item] < drink.ingredients[item]
                for item in drink.ingredients
            ]
        ):
            print("Sorry there is not enough ingredients.")
            return False
        return True

    def make_coffee(self, order):
        """
        Checks if there are enough resources to make a given drink.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy!")
