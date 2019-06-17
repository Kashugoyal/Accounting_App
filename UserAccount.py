import logging
import datetime

class UserAccount:

    frequency = {
            1: "per Day",
            15: " per 15 days",
            30 : "per month"
        }
    rate = 3.5

    def __init__(self, principal: float, start_date=None, rate: float=rate, balance :float=None, installment :float=None, duration :float=None, freq: int=1):

        self.principal = principal
        if start_date:
            self.start_date = start_date
        else:
            self.start_date = datetime.date.today()
        self.rate = rate
        self.balance = balance
        self.installment = installment
        if duration:
            # duration in months
            self.duration = duration
        else:
            self.duration = 6

        self.freq = freq
        self.loan_amount = None
        logging.info("Created new UserAccount with principal Rs: {0}".format(self.principal))

    
    def calculate_installment(self):
        
        rate = (self.rate * self.freq)/30
        t = self.duration 
        self.installment = (self.principal * rate * pow(1 + rate, t)) / (pow(1 + rate, t) - 1)
        logging.warn("UserAccount installment updated to Rs:{0} {1}".format(self.installment, UserAccount.frequency[self.freq]))


    def calculate_balance(self):
        pass

    def get(self):
        return {
            "Principal": self.principal,
            "Start Date": self.start_date,
            "Balance": self.balance,
            "Installment": self.installment,
            "Loan Duration": self.duration,
            "Frequency": self.freq }
        