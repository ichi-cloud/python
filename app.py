from flask import Flask, request, jsonify, abort
app = Flask(__name__)

@app.route('/', methods=['GET'])  # methods は省略可
def root():
    return 'hello, world'

@app.route('/jugemu/jugemu/gokono/')
def jugemu():
    return 'surikire'

@app.route('/greet/<name>')  # パスの一部を変数で受け取る1
def greet(name):
    return f'hello, {name}!'


#http://localhost:5000 をネット検索
