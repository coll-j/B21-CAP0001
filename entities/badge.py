from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Badge(db.Model, BaseModel):
    __tablename__ = 'badge'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    gambar = db.Column(db.Text, nullable=False)

    def __init__(self, title, description, gambar):
        self.title = title
        self.description = description
        self.gambar = gambar
        
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
