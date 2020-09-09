from flask import Flask, request, jsonify
from glob import escape

app = Flask(__name__)

@app.route('/<name>')
def user(name):
    return 'User %s' % escape(name)

@app.route('/')
def hello():
    return jsonify({'teste': 'asdsd'})