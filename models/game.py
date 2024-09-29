from app import db


class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)

    # Store the player IDs (list of player IDs)
    player_ids = db.Column(db.JSON, nullable=False)

    # Foreign key linking to the questions table
    current_question_id = db.Column(
        db.Integer, db.ForeignKey("questions.id"), nullable=True
    )

    # Store scores as a dictionary: {player_id: score}
    scores = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"<Game {self.id}>"
