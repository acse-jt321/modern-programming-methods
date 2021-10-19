import os

from flask import Flask, request, redirect,\
    url_for, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField

from game import PaperScissorsStone

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET',
                                'BadDefault')


CHOICES = ['paper', 'scissors', 'stone']
MAPPING = {val: key for key, val in enumerate(CHOICES)}

GAME = PaperScissorsStone()


class GameForm(FlaskForm):
    paper = SubmitField('Paper')
    scissors = SubmitField('Scissors')
    stone = SubmitField('Stone')


@app.route('/', methods=['GET', 'POST'])
def index():

    info = []
    gform = GameForm()

    if request.method == 'POST':
        choice = (MAPPING.keys() & request.form.keys()).pop()
        info.append(f'You played {choice}.')
        result, my_choice = GAME.play_round(MAPPING[choice])

        info.extend((f'I played {CHOICES[my_choice]}.',
                     f'{result}'))

    return render_template('index.html', info=info, game=GAME,
                           form=gform)
