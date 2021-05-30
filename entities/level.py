from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Level(db.Model, BaseModel):
    __tablename__ = 'level'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    branch = db.Column(db.Integer, nullable=False)
    public_link = db.Column(db.Text, nullable=False)

    def __init__(self):
        pass
