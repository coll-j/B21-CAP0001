from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Feedback(db.Model, BaseModel):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    level_id = db.Column(db.Integer, nullable=False)
    response = db.Column(db.Integer, nullable=False)
    text_feedback = db.Column(db.Text, nullable=False)

    def __init__(self):
        pass
