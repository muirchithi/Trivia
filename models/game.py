from app import db


class Game(db.Model):

    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    player_ids = db.Column(db.JSON, nullable=False)
    current_question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    scores = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"<Game {self.id}>"
