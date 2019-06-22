import logging
class UserDetails:

    def __init__(self, name, phone_number=None, address=None, reference=None):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.reference = reference

    def update(self, name=None, phone_number=None, address=None, reference=None):
        
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.reference = reference
        logging.warn("Info Updated for user: {0}".format(self.name))
    
    def get(self):
        logging.debug("Get info request received for user: {0}".format(self.name))        
        return {"Name": self.name, 
                "Phone Number": self.phone_number, 
                "Address": self.address, 
                "Reference": self.reference}