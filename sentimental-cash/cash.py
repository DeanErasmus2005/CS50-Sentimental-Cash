# TODO
from cs50 import get_float


def main():

    change_owed = get_float('Change owed: ')

    while True:
        if change_owed >= 0:
            break

        else:
             print('Please enter a non-negative integer.')

    counter = 0
    coins = [0.25, 0.10, 0.05, 0.01]
    print(change_owed)

    for coin in coins:
        while change_owed >= coin:
            change_owed = change_owed - coin
            change_owed = round(change_owed, 2)
            print(coin)
            print(change_owed)
            counter += 1
            print(counter)

    print(counter)
main()


