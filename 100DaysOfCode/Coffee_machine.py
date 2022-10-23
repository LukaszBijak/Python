
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def check_resources_for_drink(drink):
    if_is = True
    for i in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][i] < resources[i]:
            if_is = True
        else:
            if_is = False
            return print(f"Sorry there is not enough {i}.")
    return if_is


def count_coin(coins):
    sum_of_coins = 0.0
    if coins[0] > 0:
        sum_of_coins += 0.25 * coins[0]
    if coins[1] > 0:
        sum_of_coins += 0.1 * coins[1]
    if coins[2] > 0:
        sum_of_coins += 0.05 * coins[2]
    if coins[3] > 0:
        sum_of_coins += 0.01 * coins[3]
    return round(sum_of_coins, 2)


def prompt_cons():
    print(f"Please insert coins: ${MENU[user_choice]['cost']} ")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    return q, d, n, p


resources = {
    "water": 1000,
    "milk": 200,
    "coffee": 100,
}


def use_resources(drink):
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']


money_in_machine = 0.00

# ☕  🪙
machine_working = True

while machine_working:
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino) ?:"
                        "\nTurn-off - off\nPrint report - r\nYour choice: ")
    if user_choice == "r":
        print(f"\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n"
              f"Money: ${money_in_machine}\n")
    elif user_choice == "off":
        print("\nTurning off the machine...   bye!")
        machine_working = False
    elif check_resources_for_drink(user_choice):
        print(f"\nPlease insert coins: ${MENU[user_choice]['cost']} ")
        q = int(input("How many quarters?: "))
        d = int(input("How many dimes?: "))
        n = int(input("How many nickels?: "))
        p = int(input("How many pennies?: "))
        inserted_coins = [q, d, n, p]
        sum_of_inserted_coins = count_coin(inserted_coins)
        if sum_of_inserted_coins == MENU[user_choice]['cost']:
            print(f"\nHere is your {user_choice}  ☕")
            money_in_machine += sum_of_inserted_coins
            use_resources(user_choice)
        elif sum_of_inserted_coins > MENU[user_choice]['cost']:
            change = sum_of_inserted_coins - MENU[user_choice]['cost']
            money_in_machine += MENU[user_choice]['cost']
            use_resources(user_choice)
            print(f"\nHere's your change: ${round(change, 2)}")
            print(f"\nHere is your {user_choice}  ☕")
        elif sum_of_inserted_coins < MENU[user_choice]['cost']:
            print("\nSorry that's not enough money")

