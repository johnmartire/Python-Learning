MENU= {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,

        },
        "cost":1.5,

    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}
report= {
    "ingredients":{
        "water": 300,
        "milk": 200,
        "money": 0,
    }
}

while True:    
    order=input("what would you like? (espresso/latte/cappuccino): ")
    if order=="report":
        for item, value in report["Machine"].items():
            print(f"{item.capitalize()}:{value}")
    if order=="espresso":
        price=MENU["espresso"]["cost"]
    if order=="latte":
        price=MENU["latte"]["cost"]
    if order=="cappuccino":
        price=MENU["cappuccino"]["cost"]

    print("please insert coins.")
    quarter=float(0.25)
    dime=float(0.10)
    pennie=float(0.01)


    quarters=float(input("How many quarters?: "))
    dimes=float(input("How many dimes?: "))
    pennies=float(input("How many pennies?: "))
    sum1=quarters*quarter
    sum2=dimes*dime
    sum3=pennies*pennie
    total_paid=sum1+sum2+sum3
    change=total_paid-price
    if total_paid<price:
        print("Sorry thats not enough money.Money refunded")
    if change==0.0:
        print("Here is your latte ☕ enjoy!")
    if change>0.0:
        print(f"Here is {change:.2f} in change")
