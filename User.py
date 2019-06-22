import logging
from UserDetails import UserDetails
from UserAccount import UserAccount
import datetime

class User:

    num_users = 0

    @classmethod
    def get_id(cls):
        cls.num_users += 1
        return 'usr' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

    def __init__(self, name):
        
        self.user_id = User.get_id()
        self.details = UserDetails(name)
        self.remarks = ''
        self.accounts = {}
        logging.info("User created with name: {} and id: {}".format(self.details.name, self.user_id))

    def get_info(self):
        return self.details.get()

    def add_account(self, principal, start_date=datetime.date.today(), duration=UserAccount.default_duration):

        account =  UserAccount(principal, start_date, duration)
        self.accounts[account.account_id] = account
        logging.info("Account id: {0} added to user_id: {1}".format(account.account_id, self.user_id))
