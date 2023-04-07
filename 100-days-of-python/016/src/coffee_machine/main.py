"""
Simulates a coffee machine that makes espresso, latte, and cappuccino.
"""

from coffee_machine.coffee_maker import CoffeeMaker
from coffee_machine.menu import Menu
from coffee_machine.money_machine import MoneyMachine


def main():
    """
    Runs the coffee machine simulation.
    """

    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()

        if choice == "off":
            break

        if choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        drink = menu.find_drink(choice)
        if drink is None:
            continue

        if not coffee_maker.is_resource_sufficient(drink):
            continue

        if not money_machine.make_payment(drink.cost):
            continue

        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
