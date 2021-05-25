from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, BaseModel):
    uuid = db.Column(
        db.String, primary_key=True,
        unique=True, nullable=False)
    name = db.Column(db.String, nullable=True)
    username = db.Column(db.String, nullable=True)
    # email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)

    def __init__(self, username: str):
        self.username = username