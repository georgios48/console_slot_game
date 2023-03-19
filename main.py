import support


# X - your bet * 2
# Y - your bet * 5
# Z - your bet * 10

# X |                   Y |     Z
# X | <- winning line   Y |     X
# X |                   X |     Y


def restartable(func):
    def wrapper(*args, **kwargs):
        answer = 'y'
        while answer == 'y':
            func(*args, **kwargs)
            while True:
                answer = input("Play Again? y/n: ")
                if answer in ('y', 'n'):
                    break
                else:
                    print("invalid answer")
    return wrapper


@restartable
def game():
    items = ["X", "Y", "Z"]

    balance = support.get_deposit()

    while balance > 0:

        deposit, balance = support.accept_bet(balance)

        spin_machine = support.spin_machine(items)

        support.matrix_out(spin_machine)

        coef = support.check_col(spin_machine)

        balance = support.calculate_money(balance, deposit, coef)


game()
