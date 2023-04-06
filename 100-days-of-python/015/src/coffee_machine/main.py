"""
Simulates a coffee machine that makes espresso, latte, and cappuccino.
"""


from coffee_machine import coffee_maker, menu, money_machine


def main():
    """
    Runs the coffee machine simulation.
    """
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            break

        if choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        try:
            drink = menu.MENU[choice]
        except KeyError:
            print(f"Invalid input: {choice}")
            continue

        if not coffee_maker.is_resource_sufficient(drink):
            continue

        if not money_machine.make_payment(drink["cost"]):
            continue

        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
