from app import create_app, db
from models.game import Game

app = create_app()

with app.app_context():
    db.create_all()
    print("Game table created")
