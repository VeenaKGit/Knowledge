# This is a stand alone API file. This is how REST API   are written.
# All logic between a  REST API and Flask application remains the same, only difference is that REST will not
#  have UI files like static (.css etc) and templates(.html)
# Run this file and use Postman tool to verify the request.
# to send it through POSTMAN or Chrome POST add-on use the following data
# header : Content-Type , Value: application/json
# Body Raw : {"var1":"1", "var2":"2", "operator":"+"} and send as a POST request

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello to the World of API\'s'


@app.route('/math', methods=['GET', 'POST'])
def math():
    if request.json is not None:
        print("Received -", request.json)
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
        print("Not Received -", request.json)
        res = 'Request sent cannot be understood by the server'
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
