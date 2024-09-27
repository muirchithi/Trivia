from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from models.game import Game
from models.question import Question

bp = Blueprint("game", __name__)


# Route to show the game lobby
@bp.route("/lobby")
@login_required
def lobby():
    # Logic to show available games or create a new one
    return render_template("lobby.html")


# Route to start a new game
@bp.route("/start", methods=["POST"])
def start_game():
    # Logic to start a new game
    game = Game(player_ids=[current_user.id], scores={})
    db.session.add(game)
    db.session.commit()
    return redirect(url_for("game.play_game", game_id=game.id))


# Route to play the game
@bp.route("/game/<int:game_id>", methods=["GET", "POST"])
@login_required
def play_game(game_id):
    game = Game.query.get_or_404(game_id)
    question = Question.query.get(game.current_question_id)
    return render_template("game.html", question=question, game=game)
