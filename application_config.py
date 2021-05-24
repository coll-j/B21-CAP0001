from flask import Flask

from adapters.controllers.authentication import authentication

config = {"production": "config.ProdConfig", "development": "config.DevConfig", "test": "config.TestConfig"}

def create_app() -> Flask:
  app = Flask(__name__)
  app.config.from_object(config[app.config.get("ENV", "development")])

  app.register_blueprint(authentication)
  
  return app