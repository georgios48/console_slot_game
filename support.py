import random


def get_deposit():
    """Lets user enter his amount, raises error if amount <= 0"""
    balance = int(input("Balance amount: $"))

    if balance > 0:
        print(f"Your balance: {balance}$")
    else:
        raise ValueError("Wrong amount!")

    return balance


def accept_bet(balance):
    while True:
        deposit = float(input("How much do we deposit on that spin ? : "))
        if deposit > balance:
            print("no enough balance.")
        else:
            break
    balance -= deposit
    return deposit, balance


# Spins the machine and makes lines based on %
def spin_machine(items):
    spinned_items = []
    for i in range(0, 9):
        spinned_items.append("".join(random.choices([item for item in items], [18, 18, 10])))
    return spinned_items


# Checks win and calculates the coefficient
def check_win(items: list):
    win = True
    temp = items[0]
    win_mul = 0

    for item in items:
        if temp != item:
            win = False
            break
    if win:
        if temp == "X":
            win_mul += 2
        elif temp == "Y":
            win_mul += 5
        elif temp == "Z":
            win_mul += 10
    return win_mul


def check_col(items):
    win_coef = 0
    first_row = [items[0], items[3], items[6]]
    win_coef += check_win(first_row)

    second_row = [items[1], items[4], items[7]]
    win_coef += check_win(second_row)

    third_row = [items[2], items[5], items[8]]
    win_coef += check_win(third_row)

    if win_coef > 0:
        print("You win!")
    return win_coef


# Print the machine in matrix format
def matrix_out(items):
    print("\n".join([" | ".join(items[i:i + 3]) for i in range(0, len(items), 3)]))


def calculate_money(balance, deposit, coef):
    balance += deposit * coef
    print(f"Current balance: {balance} $")
    return balance
