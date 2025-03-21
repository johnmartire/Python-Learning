MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

report = {
    "ingredients": {"water": 300, "milk": 200, "coffee": 100},
    "money": 0
}

def check_ingredients(order):
    for item, amount in MENU[order]["ingredients"].items():
        if report["ingredients"].get(item, 0) < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_payment(order):
    price = MENU[order]["cost"]
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    pennies = float(input("How many pennies?: ")) * 0.01
    total_paid = quarters + dimes + pennies
    change = total_paid - price
    if total_paid < price:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        report["money"] += price
        return True

def make_coffee(order):
    for item, amount in MENU[order]["ingredients"].items():
        report["ingredients"][item] -= amount
    print(f"Here is your {order} ☕. Enjoy!")

while True:
    order = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()

    if order == "report":
        for item, value in report["ingredients"].items():
            print(f"{item.capitalize()}: {value}")
        print(f"Money: ${report['money']:.2f}")
    elif order == "exit":
        break
    elif order in MENU:
        if check_ingredients(order) and process_payment(order):
            make_coffee(order)
    else:
        print("Invalid choice, please try again.")
