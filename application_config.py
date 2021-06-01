from flask import Flask
from config import get_config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from adapters.controllers.authentication_controller import authentication
from adapters.controllers.feedback_controller import feedback
from adapters.controllers.level_controller import level
from adapters.controllers.badge_controller import badge

config = {"production": "config.ProdConfig", "development": "config.DevConfig", "test": "config.TestConfig"}
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app() -> Flask:
  app = Flask(__name__)
  app.config.from_object(get_config(None))

  db.init_app(app)
  bcrypt.init_app(app)

  app.register_blueprint(authentication)
  app.register_blueprint(feedback)
  app.register_blueprint(level)
  app.register_blueprint(badge)

  CORS(app)

  return app
