from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

from models import user, question, game
from routes import auth_routes, game_routes

# Register blueprints
app.register_blueprint(auth_routes.bp)
app.register_blueprint(game_routes.bp)

if __name__ == "__main__":
    app.run(debug=True)
