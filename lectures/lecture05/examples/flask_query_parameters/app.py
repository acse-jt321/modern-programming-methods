from flask import Flask

app = Flask(__name__)

data = {'name': ['Ling', 'George', 'Ginger'],
        'height': [1.63, 1.87, 1.34]}


@app.route("/key/<name>/data/<int:index>")
def my_func(name, index):
    return data[name][index]
