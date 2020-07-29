from flask import Blueprint, jsonify
# import requests
from src.models.projects import projects

projects_bp = Blueprint("projects_bp", __name__)


@projects_bp.route("/projects", methods=["GET"])
def get_projects():
    # requests.post('http://9c01f282b9a9.ngrok.io/', data=hintbox_projects)
    return jsonify(projects)


@projects_bp.route("/projects/<string:name>", methods=["GET"])
def get_project(name):
    project_found = [
        project for project in projects if project["name"] == name]
    if len(project_found) > 0:
        return jsonify(project_found)
    return jsonify({"message": "Not Found"})
