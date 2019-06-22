import logging
import datetime

class Transaction:

    def __init__(self, date=datetime.date.today(), expenses: dict=None, income: float=None, collector: str=None):

        self.date = date
        self.expenses = expenses
        self.income = income
        self.collector = collector


    def get(self):
        return {
            "Date" : self.date,
            "Expenses" : self.expenses,
            "Income" : self.income,
            "Collector" : self.collector
        }