from flask import Flask
from config import get_config
from flask_sqlalchemy import SQLAlchemy

from adapters.controllers.authentication_controller import authentication

config = {"production": "config.ProdConfig", "development": "config.DevConfig", "test": "config.TestConfig"}
db = SQLAlchemy()

def create_app() -> Flask:
  app = Flask(__name__)
  app.config.from_object(get_config(None))
  db.init_app(app)
  
  app.register_blueprint(authentication)
  
  return app