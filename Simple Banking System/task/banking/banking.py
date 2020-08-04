# Write your code here
from random import randrange
import sqlite3


class BankAccount:
    iin = '400000'  # issuer_identification_number

    def __init__(self):
        self.card_number = None
        self.card_pin = None
        self.create_db()
        self.main_menu()

    @staticmethod
    def create_db():
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS card('
                    '   id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    '   number TEXT NOT NULL,'
                    '   pin TEXT NOT NULL,'
                    '   balance INTEGER DEFAULT 0);')
        conn.commit()
        conn.close()

    def main_menu(self):
        while True:
            print()
            print('1. Create an account')
            print('2. Log into account')
            print('0. Exit')
            user_choice = input()
            if user_choice == '1':
                self.create_account()
            elif user_choice == '2':
                self.user_menu()
            elif user_choice == '0':
                print('Bye!')
                exit()
            else:
                print('Unknown choice, try again!')
                continue

    def user_menu(self):
        logged_user = self.log_into_account()
        while logged_user:
            print()
            print('1. Balance')
            print('2. Add income')
            print('3. Do transfer')
            print('4. Close Account')
            print('5. Log out')
            print('0. Exit')
            user_choice = input('')
            if user_choice == '1':
                print('Balance:', self.sql_balance(logged_user))
            elif user_choice == '2':
                print('Enter income:')
                income = int(input())
                print(self.sql_update_balance(logged_user, income))
                print('Income was added!')
            elif user_choice == '3':
                print('Transfer\nEnter card number:')
                destination = input()
                self.do_transfer(logged_user, destination)
            elif user_choice == '4':
                if not self.close_account(logged_user):
                    print('The account has been closed!')
                    break
            elif user_choice == '5':
                print('You have successfully logged out!')
                break
            elif user_choice == '0':
                print('Bye!')
                exit()
            else:
                print('Unknown choice, try again!')
                continue
        return self.main_menu()

    @staticmethod
    def sql_insert(card, pin):
        value = (card, pin, )
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO card(number, pin) VALUES (?, ?)', value
        )
        conn.commit()
        conn.close()

    @staticmethod
    def sql_credentials(card, pin):
        value = (card, pin)
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            'SELECT number FROM card WHERE number = ? AND pin = ?', value
        )
        result = cur.fetchone()
        conn.commit()
        conn.close()
        return True if result else False

    @staticmethod
    def sql_balance(card_number):
        value = (card_number,)
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            'SELECT balance FROM card WHERE number = ?', value
        )
        balance = cur.fetchone()
        conn.commit()
        conn.close()
        return balance[0]

    @staticmethod
    def sql_update_balance(card_number, money):
        value = (money, card_number,)
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            'UPDATE card SET balance = balance + ? WHERE number = ?', value
        )
        conn.commit()
        conn.close()
        return 'Success!'

    @staticmethod
    def sql_is_account(card_number):
        value = (card_number,)
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            'SELECT number FROM card WHERE number = ?', value
        )
        result = cur.fetchone()
        conn.commit()
        conn.close()
        return True if result else False

    def do_transfer(self, card_number, destination):
        if card_number == destination:
            print('You can\'t transfer money to the same account!')
        elif not self.is_luhn(destination):
            print('Probably you made mistake in the card number.'
                  'Please try again!')
        elif not self.sql_is_account(destination):
            print('Such a card does not exist.')
        else:
            print('Enter how much you want to transfer:')
            money = int(input())
            if self.sql_balance(card_number) < int(money):
                print('Not enough money!')
            else:
                self.sql_update_balance(card_number, -money)
                print(self.sql_update_balance(destination, money))
                print('Success!')

    def close_account(self, card_number):
        value = (card_number,)
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            'DELETE FROM card WHERE number = ?', value
        )
        conn.commit()
        conn.close()
        return self.sql_is_account(card_number)

    @staticmethod
    def luhn_sum(card_number):
        luhn_sum = 0
        for index, num in enumerate(card_number):
            if index % 2 == 1:
                luhn_sum += int(num)
            else:
                if int(num) * 2 > 9:
                    luhn_sum += int(num) * 2 - 9
                else:
                    luhn_sum += int(num) * 2
        return luhn_sum

    @staticmethod
    def is_luhn(card_number):
        luhn_sum = 0
        for index, num in enumerate(card_number):
            if index % 2 == 1:
                luhn_sum += int(num)
            else:
                if int(num) * 2 > 9:
                    luhn_sum += int(num) * 2 - 9
                else:
                    luhn_sum += int(num) * 2
        return luhn_sum % 10 == 0

    def create_account(self):
        card_number = self.generate_card_number()
        card_pin = self.generate_pin()
        self.sql_insert(self.card_number, self.card_pin)
        print('Your card has been created')
        print(f'Your card number:\n{card_number}')
        print(f'Your card PIN:\n{card_pin}')

    def generate_card_number(self):
        number = ''
        for num in range(9):
            number += str(randrange(10))
        partial_number = (self.iin + number)
        new_card_number = partial_number \
                            + self.generate_checksum(partial_number)
        self.card_number = new_card_number
        return new_card_number

    def generate_checksum(self, card_number):
        luhn_sum = self.luhn_sum(card_number)
        if luhn_sum % 10 > 0:
            return str(10 - (luhn_sum % 10))
        else:
            return '0'

    def generate_pin(self):
        new_card_pin = ''
        for num in range(4):
            new_card_pin += str(randrange(10))
        self.card_pin = new_card_pin
        return new_card_pin

    def log_into_account(self):
        username = input('Enter your card number: ')
        password = input('Enter your PIN: ')
        if self.sql_credentials(username, password):
            print('You have successfully logged in!')
            return username
        else:
            print('Wrong card number or PIN!')
            return False


# EXECUTE:)
new = BankAccount()
