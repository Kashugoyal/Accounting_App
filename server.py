from flask import Flask, make_response, request, jsonify
from flask_restful import Api, Resource, reqparse
from User import User
from UserAccount import UserAccount
from MasterAccount import MasterAccount
from db_handler import read_data, write_data
from unittest import TestCase as TC
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

account = read_data("akansal")
# write_data(account)


# account methods
@app.route('/write', methods = ['POST'])
def write_data_to_file():
    write_data(account)
    response_object = {'status': 'success'}
    response_object['file_name'] = account.name + ".json"
    return jsonify(response_object)


# user methods

@app.route('/add_user', methods = ['POST'])
def add_user():
    account.add_user(**request.args.to_dict())
    response_object = {'status': 'success'}
    response = jsonify(response_object)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_users', methods = ['GET'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def get_user_list():
    response = jsonify(account.get_users())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/user/<id>/add_account', methods = ['POST'])
def add_account(id: str):
    account_id = None
    account_id = account.users[id].add_account(**request.args.to_dict())
    status = 'success' if account_id else 'failed'
    response_object = {'status': status, 'account_id': account_id}
    return jsonify(response_object)


@app.route('/user/<id>/update', methods = ['POST'])
def update_user(id: str):
    retVal = False
    retVal = account.users[id].update_info(**request.args.to_dict())
    status = 'success' if retVal else 'failed'
    response_object = {'status': status}
    return jsonify(response_object)


@app.route('/user/<id>/get', methods = ['GET'])
def get_info(id: str):
    return jsonify(account.users[id].get_info())


@app.route('/user/<id>/get_accounts', methods = ['GET'])
def get_accounts(id: str):
    return jsonify(list(account.users[id].accounts.keys()))


@app.route('/user/<id>/remove', methods = ['POST'])
def remove_user(id: str):
    del account.users[id]
    response_object = {'status': 'success'}
    return jsonify(response_object)


#user account methods

@app.route('/user/<user_id>/<account_id>/get', methods = ['GET'])
def get_user_account(user_id: str, account_id: str):
    return jsonify(account.users[user_id].accounts[account_id].get_details())


@app.route('/user/<user_id>/<account_id>/add_payment', methods = ['POST'])
def add_user_payment(user_id: str, account_id: str):
    retVal = False
    retVal = account.users[user_id].accounts[account_id].add_payment(**request.args.to_dict())
    status = 'success' if retVal else 'failed'
    response_object = {'status': status}
    return jsonify(response_object)


# account methods

# class TestCase(TC):

#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['WTF_CSRF_ENABLED'] = False
#         app.config['DEBUG'] = False
#         self.app = app.test_client()
    
#     def tearDown(self):
#         pass
    
#     def test
        