from flask import Flask, make_response, request, jsonify
from flask_restful import Api, Resource, reqparse
from User import User
from UserAccount import UserAccount
from MasterAccount import MasterAccount

app = Flask(__name__)
api = Api(app)

account = MasterAccount()

# user methods

@app.route('/add_user', methods = ['POST'])
def add_user():
    account.add_user(**request.args.to_dict())
    response_object = {'status': 'success'}
    return jsonify(response_object)


@app.route('/user/<id>/update', methods = ['POST'])
def update_user(id):
    account.users[id].update(**request.args.to_dict())
    response_object = {'status': 'success'}
    return jsonify(response_object)


@app.route('/user/<id>/remove')
def remove_user(id):
    del account.users[id]
    response_object = {'status': 'success'}
    return jsonify(response_object)


@app.route('/user/<id>/add_account')
def add_user_account(id):
    account.users[id].add_account(**request.args.to_dict())


# account methods

@app.route('/get_users', methods = ['GET'])
def get_user_list():
    return jsonify(account.get_users())
