from app import app

from flask import render_template, request, redirect

from app.models.src.player import Player
from app.models.src.game import Game, ai_choice
from app.models.src.results import Results

results = Results()


@app.route("/")
def index():
    return render_template("pvp.html", title="Home", results = results)

@app.route("/rules")
def rules():
    return render_template("rules.html", title="Rules")

@app.route("/player-vs-player")
def pvp():
    return render_template("pvp.html", title="Player Vs Player", results=results)

@app.route("/player-vs-ai")
def pvc():
    return render_template("pvc.html", title="Player Vs Computer", results=results)

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
    results.ai_check = request.form["ai-check"]
    player_1_name = request.form["player-1-name"]
    player_1_choice = request.form["player-1-choice"]
    if results.ai_check:
        player_2_name = "Skynet"
        player_2_choice = ai_choice()
    else:
        player_2_name = request.form["player-2-name"]
        player_2_choice = request.form["player-2-choice"]
    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)
    game = Game(player_1, player_2)
    game.play_game(results)
    print(results.ai_check)
    if results.ai_check == "True":
        return redirect("/player-vs-ai")
    elif results.ai_check == "False":
        return redirect("/player-vs-player")

@app.route("/reset-scores", methods=["POST"])
def reset_scores():
    results.ai_check = request.form["ai-check2"]
    results.reset_scores()
    if results.ai_check == "True":
        return redirect("/player-vs-ai")
    elif results.ai_check == "False":
        return redirect("/player-vs-player")