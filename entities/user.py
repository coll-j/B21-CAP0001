from entities.blacklisted_tokens import BlacklistToken
from flask_bcrypt import Bcrypt
from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()
SECRET_KEY="THUMBSGENGS"


class User(db.Model, BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(password, 13).decode()

    def encode_auth_token(self, id):
        try:
            payload = {
                'exp':
                datetime.datetime.utcnow() +
                datetime.timedelta(days=1, seconds=5),
                'iat':
                datetime.datetime.utcnow(),
                'sub':
                id
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
      Validates the auth token
      :param auth_token:
      :return: integer|string
      """
        try:
            payload = jwt.decode(
                auth_token,
                SECRET_KEY,
                algorithms=["HS256"]
            )
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
              return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
