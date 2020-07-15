from flask import Flask
import requests

from .config import app_config
from .routes.projects_route import projects_bp


def create_app(env_name):

    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    app.register_blueprint(projects_bp)

    @app.route('/')
    def index():
        return "ja"

    return app
