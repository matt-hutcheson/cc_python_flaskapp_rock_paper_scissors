from app import app

from flask import render_template

from app.models.src.player import *
from app.models.src.game import *

@app.route('/')
def index():
    return render_template("base.html", title="Home")