import logging
from UserAccount import UserAccount
import datetime
import uuid

class User:

    num_users = 0

    @classmethod
    def get_id(cls, name: str):
        cls.num_users += 1
        return 'usr{:04d}{}'.format(cls.num_users, name)

    def __init__(self, **kwargs):
        
        try:
            self.name = kwargs.get('name')
        except KeyError:
            logging.error("Invalid Name for the user. Try again.")
            return
        self.user_id = kwargs.get('user_id', User.get_id(self.name))
        self.phone_number = kwargs.get('phone_number', '')
        self.address = kwargs.get('address', '')
        self.reference = kwargs.get('reference', '')
        self.remarks = kwargs.get('remarks', '')
        self.accounts = {}
        logging.info("User created with name: {} and id: {}".format(self.name, self.user_id))

    def add_account(self, **kwargs):

        try:
            principal = kwargs.get('principal')
        except KeyError:
            logging.error("Principal value not given. Could not add the account.")
            return None
        account =  UserAccount(**kwargs)
        self.accounts[account.account_id] = account
        logging.info("Account id: {0} added to user_id: {1}".format(account.account_id, self.user_id))
        return account.account_id

    def update_info(self, **kwargs):
        
        self.name = kwargs.get('name', '')
        self.phone_number = kwargs.get('phone_number', '')
        self.address = kwargs.get('address', '')
        self.reference = kwargs.get('reference', '')
        logging.warn("Info Updated for user: {0}".format(self.name))
        return True

    def get_info(self):
        logging.debug("Get info request received for user: {0}".format(self.name))        
        return {"name": self.name, 
                "phone Number": self.phone_number, 
                "address": self.address, 
                "reference": self.reference,
                "remarks": self.remarks}
    
    def get_accounts(self):
        return self.accounts.keys()