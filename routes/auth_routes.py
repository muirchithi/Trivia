from flask import Blueprint

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    return "Login Page"


@bp.route("/register", methods=["GET", "POST"])
def register():
    return "Register Page"
