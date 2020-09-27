from flask import Flask
from config import config_options


def create_app(config_name):

  app = Flask(__name__)

  # Creating the app configurations
  app.config.from_object(config_options[config_name])


  # Registering the blueprints
  from .blog import blog as blog_blueprint
  app.register_blueprint(blog_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

  from .requests import configure_request
  configure_request(app)

  return app