import logging
from UserAccount import UserAccount
import datetime

class User:

    num_users = 0

    @classmethod
    def get_id(cls):
        cls.num_users += 1
        return 'usr' + datetime.datetime.now().strftime('%m%d%H%M%S%f')

    def __init__(self, **kwargs):
        
        self.user_id = User.get_id()
        try:
            self.name = kwargs.get('Name')
        except KeyError:
            logging.error("Invalid Name for the user. Try again.")
            return
        self.phone_number = kwargs.get('PhoneNumber', None)
        self.address = kwargs.get('Address', '')
        self.reference = kwargs.get('Reference', '')
        self.remarks = ''
        self.accounts = {}
        logging.info("User created with name: {} and id: {}".format(self.name, self.user_id))

    def add_account(self, **kwargs):

        try:
            principal = kwargs.get('Principal')
        except KeyError:
            logging.error("Principal value not given. Could not add the account.")
            return None
        account =  UserAccount(principal, **kwargs)
        self.accounts[account.account_id] = account
        logging.info("Account id: {0} added to user_id: {1}".format(account.account_id, self.user_id))
        return account.account_id

    def update_info(self, **kwargs):
        
        self.name = kwargs.get('Name', '')
        self.phone_number = kwargs.get('Phone_number', '')
        self.address = kwargs.get('Address', '')
        self.reference = kwargs.get('Reference', '')
        logging.warn("Info Updated for user: {0}".format(self.name))
        return True

    def get_info(self):
        logging.debug("Get info request received for user: {0}".format(self.name))        
        return {"Name": self.name, 
                "Phone Number": self.phone_number, 
                "Address": self.address, 
                "Reference": self.reference}
    
    def get_accounts(self):
        return self.accounts.keys()