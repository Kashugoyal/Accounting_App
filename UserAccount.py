import logging
import datetime

class UserAccount:

    frequency = {
            1: "per Day",
            15: " per 15 days",
            30: "per month",
            45: "45 days",
            60: "every 2 months",
            180: "every 6 months"
        }
    rate = 3.5

    num_accounts = 0
    default_duration = 6

    @classmethod
    def get_id(cls):
        cls.num_accounts += 1
        return 'acc' + datetime.datetime.now().strftime('%m%d%H%M%S%f')


    def __init__(self,
                 principal: float,
                 start_date=datetime.date.today(),
                 rate: float=rate,
                 balance :float=None, 
                 installment :float=None, 
                 duration :float=default_duration, 
                 freq: int=1):

        self.account_id = UserAccount.get_id()
        # in Rs
        self.principal = principal
        self.start_date = start_date
        # interest per month
        self.rate = rate
        # in Rs
        self.balance = balance
        # in Rs
        self.installment = installment
        # time period in months
        self.duration = duration
        # payment frequency - once a month, twice a month etc.
        self.freq = freq
        # principal + interest
        self.loan_amount = None
        self.payments = {}
        logging.info("Created new UserAccount with principal Rs: {0}".format(self.principal))


    def calculate_installment(self):
        rate = self.rate
        t = 30/self.freq
        self.installment = (self.principal * rate * pow(1 + rate, t)) / (pow(1 + rate, t) - 1)
        self.loan_amount = self.installment*self.duration*30/self.freq
        logging.warn("UserAccount installment updated to Rs:{0} {1}".format(self.installment, UserAccount.frequency[self.freq]))


    def calculate_balance(self):
        self.balance = self.loan_amount - sum(self.payments.keys())


    def update_account(self, **kwargs):
        self.principal = kwargs.get("principal", self.principal)
        self.start_date = kwargs.get("sart_date", self.start_date)
        self.rate = kwargs.get("rate", self.rate)
        self.duration = kwargs.get("duration", self.duration)
        self.freq = kwargs.get("freq", self.freq)
        self.calculate_installment()
        return True


    def get_account(self):
        return {
            "principal": self.principal,
            "start_date": self.start_date,
            "balance": self.balance,
            "installment": self.installment,
            "duration": self.duration,
            "loan_amount": self.loan_amount,
            "freq": self.freq }


    def add_payment(self, value, date=datetime.date.today()):
        self.payments[date] = value
        self.calculate_balance()
        