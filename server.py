from flask import Flask, make_response, request
from flask_restful import Api, Resource, reqparse
from User import User
from UserAccount import UserAccount

app = Flask(__name__)
api = Api(app)


def process(req):
    hello = ''
    print(req)

@app.route('/add_user', methods = ['POST', 'PUT'])
def add_user():
    if request.method == 'POST':
        process(request)
        return make_response('Received')
    else:
        return make_response("Did not")


