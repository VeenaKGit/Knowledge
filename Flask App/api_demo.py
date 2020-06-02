# This is a stand alone API file.
# Run this file and use Postman tool to verify the request.

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello to the World of API\'s'


@app.route('/math', methods=['GET', 'POST'])
def math():
    if request.json is not None:
        op = request.json['operator']
        var1 = int(request.json['var1'])
        var2 = int(request.json['var2'])
        if op == '+':
            res = var1 + var2
        elif op == '-':
            res = var1 - var2
        elif op == '*':
            res = var1 * var2
        elif op == '/':
            res = var1 / var2
        else:
            res = 'Operator Error'
    else:
        res = 'Request sent cannot be understood by the server'
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)