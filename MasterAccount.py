import logging
import datetime
from User import User
from DailyTransaction import Transaction

class MasterAccount:

    def __init__(self):
        self.users = []
        self.num_users = None
        self.loaned_sum = None
        self.transactions = {}

    def add_user(self, name, principal, duration):
        id = 10
        user = User(id, name, principal, duration)
        self.users.append(user)
        self.num_users += 1


    def add_transaction(self, date, expenses, income, collector):
        transaction = Transaction(date, expenses, income, collector)
        self.transactions[date] = transaction


