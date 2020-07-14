from flask import Flask
import requests

from .config import app_config


def create_app(env_name):

    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    @app.route('/')
    def index():
        requests.post("https://2eed470110cb.ngrok.io", data="Hola")
        return "Listo"

    return app
