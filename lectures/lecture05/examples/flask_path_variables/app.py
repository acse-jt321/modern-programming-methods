from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def my_func():
    return "<b>Hello</b> World!"
