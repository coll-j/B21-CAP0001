from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Fact(db.Model, BaseModel):
    __tablename__ = 'facts'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    question_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, question_id, text):
        self.question_id = level_id
        self.text = text

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
