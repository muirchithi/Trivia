from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import sqlite3

# Initialize the SQLAlchemy instance
db = SQLAlchemy()


def create_app():
    # Create a Flask app instance
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object("config.Config")

    # Initialize the app with SQLAlchemy
    db.init_app(app)

    # Set up Flask-Login
    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from models.user import User

        return User.query.get(int(user_id))

    # Import and register blueprints
    from models import user, question, game
    from routes import auth_routes, game_routes

    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(game_routes.bp)

    return app


def create_sqlite_database(filename):
    """create a database connection to an SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# Only run the app if this script is executed directly
if __name__ == "__main__":
    create_sqlite_database("Trivia.db")
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
