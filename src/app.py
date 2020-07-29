from flask import Flask, jsonify
from .config import app_config
from .routes.projects_route import projects_bp
from .routes.members_route import members_bp


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    app.config["JSON_SORT_KEYS"] = False
    app.register_blueprint(projects_bp)
    app.register_blueprint(members_bp)

    @app.route("/")
    def index():
        return jsonify(
            {
                "HintBoxAPI": {
                    "name": "HintBoxAPI",
                    "version": "0.0.1",
                    "routes": [
                        "/projects",
                        "/members"],
                }
            }
        )

    return app
