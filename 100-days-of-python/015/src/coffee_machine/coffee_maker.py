"""
Provides a set of functions for checking resource sufficiency, making coffee,
and generating a report on the coffee machine's resources.
"""


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(drink):
    """
    Checks if there are enough resources to make a given drink.
    """
    order_ingredients = drink["ingredients"]
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(drink):
    """
    Makes a drink and updates resource values.
    """
    order_ingredients = drink["ingredients"]
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink['name']}. Enjoy!")


def report():
    """
    Prints the current resources values.
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
