from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user
from werkzeug.security import check_password_hash

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    from models.user import User  # Move import here to avoid circular import

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("game.lobby"))
        else:
            flash("Invalid username or password")
            return redirect(url_for("auth.login"))

    return render_template("login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    return "Register Page"
