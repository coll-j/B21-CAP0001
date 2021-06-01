from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Question(db.Model, BaseModel):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    level_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    is_multiple_choices = db.Column(db.Boolean, nullable=False)

    def __init__(self, level_id, text, is_multiple_choices):
        self.level_id = level_id
        self.text = text
        self.is_multiple_choices = is_multiple_choices

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
