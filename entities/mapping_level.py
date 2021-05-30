from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MappingLevel(db.Model, BaseModel):
    __tablename__ = 'mapping_level'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    level_before = db.Column(db.Integer, nullable=False)
    level_next = db.Column(db.Integer, nullable=False)

    def __init__(self):
        pass
