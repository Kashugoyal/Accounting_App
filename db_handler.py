import json
import logging
from MasterAccount import MasterAccount
from User import User
from UserAccount import UserAccount

# helper functions to load data
def read_process_user_account(data: dict):
    account = UserAccount(**data)
    for key, item in data["payments"].items():
        account.add_payment(item, key)
    return account

def read_process_user(data: dict):
    user = User(**data)
    for key, item in data["accounts"].items():
        user.accounts[key] = read_process_user_account(item)
    return user

def read_process_account(data: dict):
    account = MasterAccount(**data)
    for key, item in data["users"].items():
        account.users[key] = read_process_user(item)
    return account


# helper functions to unload data to json
def write_process_user_account(data):
    dump = {}
    dump["account_id"] = data.account_id
    dump["principal"] = data.principal
    dump["start_date"] = data.start_date
    dump["rate"] = data.rate
    dump["balance"] = data.balance
    dump["installment"] = data.installment
    dump["duration"] = data.duration
    dump["freq"] = data.freq
    dump["loan_amount"] = data.loan_amount
    dump["payments"] = data.payments
    return dump

def write_process_user(data):
    dump = {}
    dump["user_id"] = data.user_id
    dump["name"] = data.name
    dump["phone_number"] = data.phone_number
    dump["address"] = data.address
    dump["reference"] = data.reference
    dump["remarks"] = data.remarks
    accounts = {}
    for key, item in data.accounts.items():
        account = write_process_user_account(item)
        accounts[key] = account
    dump["accounts"] = accounts
    return dump

def write_process_account(data):
    dump = {}
    dump["name"] = data.name
    dump["user_array"] = data.user_array
    dump["loaned_sum"] = data.loaned_sum
    users = {}
    for key, item in data.users.items():
        user = write_process_user(item)
        users[key] = user
    dump["users"] = users
    return dump


# read data from file and load into memory
def read_data(account_name: str):
    file_name = account_name + ".json"
    with open(file_name, "r") as dump_file:
        data = json.load(dump_file)
        account = read_process_account(data)
    logging.warn("Successfully loaded data from file: {}".format(file_name))
    return account


# write data from memory to file
def write_data(data: MasterAccount):
    file_name = data.name + ".json"
    dump = write_process_account(data)
    with open(file_name, "w") as dump_file:
        json.dump(dump, dump_file, indent=4)
    logging.warn("Successfully written data to file: {}".format(file_name))



