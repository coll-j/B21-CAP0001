from flask_bcrypt import Bcrypt
from .abc import BaseModel
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()


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
                datetime.timedelta(days=0, seconds=5),
                'iat':
                datetime.datetime.utcnow(),
                'sub':
                id
            }
            return jwt.encode(
                payload,
                "\xa1R}\xfb\xf3W\xdc\x7f\x94\x92\xc2R\xa9\xe4\x81\x0e\xa3\xb0\xf9q\xa4\xf4\xdd\xe3",
                algorithm='HS256')
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
                "\xa1R}\xfb\xf3W\xdc\x7f\x94\x92\xc2R\xa9\xe4\x81\x0e\xa3\xb0\xf9q\xa4\xf4\xdd\xe3"
            )
            # is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            # if is_blacklisted_token:
            #     return 'Token blacklisted. Please log in again.'
            # else:
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
