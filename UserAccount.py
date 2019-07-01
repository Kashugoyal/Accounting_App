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
    default_duration = 6.0

    @classmethod
    def get_id(cls):
        cls.num_accounts += 1
        return 'acc' + datetime.datetime.now().strftime('%j%H%M%S%f')


    def __init__(self, **kwargs):

        self.account_id = kwargs.get('account_id', UserAccount.get_id())
        # in Rs
        self.principal = float(kwargs.get("principal", 0))
        self.start_date = kwargs.get("start_date", f"{datetime.datetime.now():%Y-%m-%d}")
        # interest per month
        self.rate = float(kwargs.get("rate", UserAccount.rate))
        # in Rs
        self.balance = float(kwargs.get("balance", 0))
        # in Rs
        self.installment = float(kwargs.get("installment", 0))
        # time period in months
        self.duration = float(kwargs.get("duration",  UserAccount.default_duration))
        # payment frequency - once a month, twice a month etc.
        self.freq = int(kwargs.get("freq", 1))

        # principal + interest
        self.loan_amount = float(kwargs.get("loan_amount", 0))

        self.payments = {}
        self.calculate_installment()
        self.calculate_balance()
        logging.info("Created new UserAccount with principal Rs: {0}".format(self.principal))


    def calculate_installment(self):
        rate = self.rate
        t = self.duration
        installment = (self.principal * rate * pow(1 + rate, t)) / (pow(1 + rate, t) - 1)
        self.installment = installment*self.freq/30
        self.loan_amount = self.installment*self.duration*30/self.freq
        logging.warn("UserAccount {2} installment updated to Rs:{0} {1}".format(self.installment, UserAccount.frequency[self.freq], self.account_id))


    def calculate_balance(self):
        self.balance = self.loan_amount - sum(self.payments.values())


    def update_account(self, **kwargs):
        self.principal = kwargs.get("principal", self.principal)
        self.start_date = kwargs.get("sart_date", self.start_date)
        self.rate = kwargs.get("rate", self.rate)
        self.duration = kwargs.get("duration", self.duration)
        self.freq = kwargs.get("freq", self.freq)
        self.calculate_installment()
        return True


    def get_details(self):
        return {
            "principal": self.principal,
            "start_date": self.start_date,
            "balance": self.balance,
            "installment": self.installment,
            "duration": self.duration,
            "rate": self.rate,
            "loan_amount": self.loan_amount,
            "freq": self.freq,
            "payments": self.payments }


    def add_payment(self, value, date=datetime.date.today()):
        self.payments[date] = float(value)
        self.calculate_balance()
        return True
        