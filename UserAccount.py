import logging
import datetime

class UserAccount:

    frequency = {
            1: "per Day",
            15: " per 15 days",
            30 : "per month"
        }
    rate = 3.5

    num_accounts = 0
    default_duration = 6

    @classmethod
    def get_id(cls):
        cls.num_accounts += 1
        return 'acc' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')


    def __init__(self,
                 principal: float,
                 start_date=datetime.date.today(),
                 rate: float=rate,
                 balance :float=None, 
                 installment :float=None, 
                 duration :float=default_duration, 
                 freq: int=1):

        self.account_id = UserAccount.get_id()
        self.principal = principal
        self.start_date = start_date
        self.rate = rate
        self.balance = balance
        self.installment = installment
        self.duration = duration
        self.freq = freq
        self.loan_amount = None
        self.payments = {}
        logging.info("Created new UserAccount with principal Rs: {0}".format(self.principal))

    
    def calculate_installment(self):
        
        rate = (self.rate * self.freq)/30
        t = self.duration 
        self.installment = (self.principal * rate * pow(1 + rate, t)) / (pow(1 + rate, t) - 1)
        logging.warn("UserAccount installment updated to Rs:{0} {1}".format(self.installment, UserAccount.frequency[self.freq]))


    def calculate_balance(self):
        pass

    def add_payment(self, value, date=datetime.date.today()):
        self.payments[date] = value
        self.calculate_balance()

    def get(self):
        return {
            "Principal": self.principal,
            "Start Date": self.start_date,
            "Balance": self.balance,
            "Installment": self.installment,
            "Loan Duration": self.duration,
            "Frequency": self.freq }
        