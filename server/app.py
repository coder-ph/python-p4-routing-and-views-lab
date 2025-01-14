#!/usr/bin/env python3

from flask import Flask, make_response

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
    return make_response(result)

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
                return make_response("Division by zero is not allowed.", status=400)
            result = num1 / num2
        elif operation == '%':
            if num2 == 0:
                return make_response("Modulo by zero is not allowed.", status=400)
            result = num1 % num2
        else:
            return make_response("Invalid operation. Supported operations are +, -, *, div, and %.", status=400)
        
        
        return make_response(str(result))

    except Exception as e:
        
        return make_response(f"Error: {e}", status=500)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
