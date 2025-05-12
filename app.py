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



if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

#http://localhost:5000 をネット検索
