# Write your code here
from random import randrange
import sqlite3


class BankAccount:
    iin = '400000'  # issuer_identification_number

    def __init__(self):
        self.card_number = None
        self.card_pin = None
        self.create_db()
        self.main()

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

    @staticmethod
    def main_menu():
        choice = input('1. Create an account\n2. Log into account\n0. Exit')
        return int(choice)

    @staticmethod
    def user_menu():
        choice = input('1. Balance\n2. Log out\n0. Exit')
        return int(choice)

    @staticmethod
    def sql_insert(card, pin):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            f'INSERT INTO'
            f'  card(number, pin)'
            f'VALUES'
            f'  ({card}, {pin})'
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
        value = (card_number, )
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
    def luhn(card_number):
        luhn_sum = 0
        for index, num in enumerate(card_number):
            if index % 2 == 0:
                if int(num) * 2 > 9:
                    luhn_sum += int(num) * 2 - 9
                else:
                    luhn_sum += int(num) * 2
            else:
                luhn_sum += int(num)
        return luhn_sum

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
        luhn_sum = self.luhn(card_number)
        if luhn_sum % 10 > 0:
            return str(10 - (self.luhn(card_number) % 10))
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

    def main(self):
        while True:
            choice1 = self.main_menu()
            if choice1 == 1:
                self.create_account()
            elif choice1 == 2:
                logged_user = self.log_into_account()
                while logged_user:
                    choice2 = self.user_menu()
                    if choice2 == 1:
                        print(self.sql_balance(logged_user))
                    elif choice2 == 2:
                        print('You have successfully logged out!')
                        break
                    else:
                        print('Bye!')
                        exit()
            else:
                print('Bye!')
                exit()


# EXECUTE:)

new = BankAccount()
