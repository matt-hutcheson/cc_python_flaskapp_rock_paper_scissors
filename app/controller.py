from app import app

from flask import render_template

from app.models.src.player import *
from app.models.src.game import *

@app.route('/')
def index():
    return render_template("base.html", title="Home")

@app.route('<name_1>/<choice_1>/<name_2>/<choice_2>')
def result(name_1,choice_1,name_2,choice_2):
    player_1 = Player(name_1,choice_1)
    player_2 = Player(name_2,choice_2)
    game = Game(player_1,player_2)
    return game.play_game()