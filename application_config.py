from flask import Flask
from config import get_config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from adapters.controllers.authentication_controller import authentication

config = {"production": "config.ProdConfig", "development": "config.DevConfig", "test": "config.TestConfig"}
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app() -> Flask:
  app = Flask(__name__)
  app.config.from_object(get_config(None))
  
  db.init_app(app)
  bcrypt.init_app(app)
  
  app.register_blueprint(authentication)

  CORS(app)

  return app