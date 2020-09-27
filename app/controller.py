from app import app

from flask import render_template, request, redirect

from app.models.src.player import Player
from app.models.src.game import Game
from app.models.src.results import Results

results = Results()

@app.route("/")
def index():
    return render_template("base.html", title="Home", results = results)

@app.route("/<name_1>/<choice_1>/<name_2>/<choice_2>")
def result(name_1,choice_1,name_2,choice_2):
    player_1 = Player(name_1,choice_1)
    player_2 = Player(name_2,choice_2)
    game = Game(player_1,player_2)
    url_results = Results()
    game.play_game(url_results)
    return url_results.result

@app.route("/play-game", methods=["POST"])
def play_game():
    player_1_name = request.form["player-1-name"]
    player_1_choice = request.form["player-1-choice"]
    player_2_name = request.form["player-2-name"]
    player_2_choice = request.form["player-2-choice"]
    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)
    game = Game(player_1, player_2)
    game.play_game(results)
    return redirect('/')