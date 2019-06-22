import logging
import datetime
from User import User
from DailyTransaction import Transaction

class MasterAccount:

    def __init__(self):
        self.user_array = []
        self.loaned_sum = None
        self.transactions = {}
        self.users = {}

    def add_user(self, id_num, name, principal, duration):
        self.users[id_num] = User(id_num, name, principal, duration)
        self.user_array.append(id_num)

    def del_user(self, id_num):
        self.user_array.remove(id_num)
        self.users.pop(id_num, None)


    def add_transaction(self, date, expenses, income, collector):
        for key in income.keys():
            self.users[key].account.add_payment(income[key], date)
            logging.info('Added payment of Rs. {0} for User ID: {1}'.format(income[key], key))
        self.transactions[date] = Transaction(date, expenses, income, collector)


