from app import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500), nullable=False)
    options = db.Column(db.JSON, nullable=False)
    correct_answer = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<Question {self.id}>"
