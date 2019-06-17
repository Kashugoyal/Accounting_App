import logging
from UserDetails import UserDetails
from UserAccount import UserAccount
import datetime

class User:

    def __init__(self, id, name, principal, duration, start_date=datetime.date.today()):
        
        self.id = id
        self.details = UserDetails(name)
        self.account = UserAccount(principal, start_date=start_date, duration=duration)

        logging.info("User created with name: {} and id: {}".format(self.details.name, self.id))

    
    def get_info(self):
        return self.details.get()
