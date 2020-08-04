# Write your code here
from random import randrange


class BankAccount:
    issuer_identification_number = '400000'
    balance = 0
    accounts = {}

    def __init__(self):
        self.card_number = None
        self.card_pin = None
        self.main()

    def luhn(self, card_number):
        verify_number = card_number[:15]
        luhn_sum = 0
        for index, num in enumerate(verify_number):
            if index % 2 == 0:
                if int(num) * 2 > 9:
                    luhn_sum += int(num) * 2 - 9
                else:
                    luhn_sum += int(num) * 2
            else:
                luhn_sum += int(num)
        return luhn_sum

    def generate_checksum(self, card_number):
        luhn_sum = self.luhn(card_number)
        if luhn_sum % 10 > 0:
            return str(10 - (self.luhn(card_number) % 10))
        else:
            return '0'

    def generate_account_number(self):
        number = ''
        for num in range(9):
            number += str(randrange(10))
        return number

    def generate_card_number(self):
        partial_number = (self.issuer_identification_number
                          + self.generate_account_number())
        new_card_number = partial_number + self.generate_checksum(partial_number)
        return new_card_number

    def generate_pin(self):
        new_card_pin = ''
        for num in range(4):
            new_card_pin += str(randrange(10))
        return new_card_pin

    def create_account(self):
        card_number = self.generate_card_number()
        card_pin = self.generate_pin()
        self.accounts[card_number] =\
            {'pin': card_pin, 'balance': self.balance}
        print('Your card has been created')
        print(f'Your card number:\n{card_number}')
        print(f'Your card PIN:\n{card_pin}')

    def log_into_account(self):
        username = input('Enter your card number: ')
        password = input('Enter your PIN: ')
        if username in self.accounts and \
                password == self.accounts[username]['pin']:
            print('You have successfully logged in!')
            return username
        else:
            print('Wrong card number or PIN!')
            return False

    def main_menu(self):
        choice = input('1. Create an account\n2. Log into account\n0. Exit')
        return int(choice)

    def user_menu(self):
        choice = input('1. Balance\n2. Log out\n0. Exit')
        return int(choice)

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
                        print(f'Balance '
                              f'{self.accounts[logged_user]["balance"]}')
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
