from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserResponse(db.Model, BaseModel):
    __tablename__ = 'user_response'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    level_id = db.Column(db.Integer, nullable=False)
    response_text = db.Column(db.Text, nullable=False)
    response_option = db.Column(db.BigInteger, nullable=True)
    response_prediction_result = db.Column(db.BigInteger, nullable=False)

    def __init__(self):
        pass
