import logging
import datetime
from User import User
# from DailyTransaction import Transaction

class MasterAccount:

    def __init__(self):
        self.user_array = []
        self.loaned_sum = None
        # self.transactions = {}
        self.users = {}

    def add_user(self, **kwargs):
        user = User(**kwargs)
        self.users[user.user_id] = user
        self.user_array.append(user.user_id)

    # def del_user(self, user_id):
    #     self.user_array.remove(user_id)
    #     self.users.pop(user_id, None)

    def get_users(self):
        return [(user.id, user.name) for user in self.users.values()]

    # def add_transaction(self, date, expenses, income, collector):
    #     for key in income.keys():
    #         self.users[key].account.add_payment(income[key], date)
    #         logging.info('Added payment of Rs. {0} for User ID: {1}'.format(income[key], key))
    #     self.transactions[date] = Transaction(date, expenses, income, collector)


