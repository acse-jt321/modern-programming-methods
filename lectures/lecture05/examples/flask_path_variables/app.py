from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/hello")
def my_func():
    return "<b>Hello</b> World!"


@app.route("/cat")
def my_fun1():
    return "Meow"


@app.route("/name/<input_name>/age/<int:input_age>")
def my_fun2(input_name,input_age):
    return f"<b>Hello</b> {input_name}! Looking good for {input_age}!"

@app.route("/client")
def my_func3():
    client_name = request.args.get('name',default=None)
    if client_name in clients:
        return f"<b>Hello</b> {client_name}!"
    else:
        return f"Are you in the right place?"
