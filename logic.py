from random import randint
from decouple import config

def select_slot():
    while True:
        try:
            selected_slot = int(input('Выбери слот от 1 до 30: '))
            if 1 <= selected_slot <= 30:
                return selected_slot
            else:
                print('Я попросил от 1 до 30, повтори :')
        except ValueError:
            print('Введи целое число, а не то что ты пишешь: ')

def place_bet(balance):
    while True:
        try:
            bet = int(input(f'Ваш баланс: {balance}$. Сделайте ставку: '))
            if bet <= 0 or bet > balance:
                print('Нехватает баланса. Повтори: ')
                continue
            return bet
        except ValueError:
            print('Введи целое число, а не то что ты пишешь: ')

def spin_wheel():
    return randint(1, 30)

def update_balance(balance, bet, win):
    if win:
        balance += bet * 2
    else:
        balance -= bet
    return balance

def determine_win(selected_slot, winning_slot):
    return selected_slot == winning_slot

def play_game():
    initial_money = int(config('MY_MONEY'))
    balance = initial_money

    while True:
        while balance > 0:
            selected_slot = select_slot()
            bet = place_bet(balance)
            winning_slot = spin_wheel()
            win = determine_win(selected_slot, winning_slot)
            balance = update_balance(balance, bet, win)

            if win:
                print(f'Везет, ты выйграл {bet * 2}$')
            else:
                print(f'Твой проигрыш {bet}$')
                print(f'Выигрышный слот: {winning_slot}')

            play_again = input('Повторим? выбери Y или N: ').lower()
            if play_again != 'y':
                break

        print(f'Игра завершена. Ваш конечный баланс: {balance}$')
        break
