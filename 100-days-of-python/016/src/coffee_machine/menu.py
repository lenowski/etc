"""
Contains the MenuItem and Menu classes, which provides functionality to
create and access menu items in a coffee machine.
"""


class MenuItem:
    """
    Models a menu item with a name, ingredients, and cost.
    """

    def __init__(self, name, water, milk, coffee, cost):
        """
        Initializes a new instance with default resources.
        """
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    """
    Models a menu with a list of menu items, and provides methods
    to get the items and find a specific item by name.
    """

    def __init__(self):
        """
        Initializes a new instance with default menu items.
        """
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """
        Returns a string with the names of all available menu items.
        """
        return "/".join([item.name for item in self.menu])

    def find_drink(self, order_name):
        """
        Returns the MenuItem object that matches the given order name,
        or prints an error message and returns None if not found.
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None
