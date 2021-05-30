from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserLevels(db.Model, BaseModel):
    __tablename__ = 'user_levels'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    level_id = db.Column(db.Integer, nullable=False)

    def __init__(self):
        pass
