from flask import Flask
from flask import request
from flask import Response
from flask import jsonify

app = Flask(__name__)

d={}
count=1

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    global count
    name = request.form["name"]
    d[str(count)] =  name
    data = {
        'id'  : count,
        'name' : name
    }
    resp = jsonify(data)
    resp.status_code = 201
    count = count + 1
    return resp

@app.route('/users/<username>', methods=['GET'])
def display_user(username):

    name = d.get(username)
    if name is None:
        resp = jsonify("")
        resp.status_code = 404
        return resp
    else:
        data = {
        'id'  : username,
        'name' : name
        }
        resp = jsonify(data)
        resp.status_code = 200
        return resp

@app.route('/users/<username>', methods=['DELETE'])
def del_users(username):
    del d[username]
    resp = jsonify("")
    resp.status_code = 204
    return resp
