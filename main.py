from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_report = MoneyMachine()

flag = True
while flag:
    user_choice = input(f"What would you like? ({menu.get_items()}):")
    if user_choice == "Report":
        coffee_maker.report()
        money_report.report()
    elif user_choice == "Off":
        print("Bye")
        flag = False
    else:
        menu_item = menu.find_drink(user_choice)
        if menu_item is not None:
            able_to_dispense = coffee_maker.is_resource_sufficient(menu_item)
            if able_to_dispense:
                if money_report.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)