#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str>')
def print_string(str):
    print(f'{str}')
    return str

@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(param))
    result = f"{numbers}\n"
    return Response(result, mimetype="text/plain")

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation,num2):
    try:
        # Perform the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return Response("Division by zero is not allowed.", status=400, mimetype="text/plain")
            result = num1 / num2
        elif operation == '%':
            if num2 == 0:
                return Response("Modulo by zero is not allowed.", status=400, mimetype="text/plain")
            result = num1 % num2
        else:
            return Response("Invalid operation. Supported operations are +, -, *, div, and %.", status=400, mimetype="text/plain")
        
        
        return Response(str(result), mimetype="text/plain")

    except Exception as e:
        
        return Response(f"Error: {e}", status=500, mimetype="text/plain")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
