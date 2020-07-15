from flask import Blueprint, jsonify
import requests

from src.models.projects import hint_projects


projects_bp = Blueprint('projects_bp', __name__)

projects = requests.get('https://api.github.com/orgs/Hint-Box/repos')


@projects_bp.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(hint_projects)


@projects_bp.route('/projects/<string:name>', methods=['GET'])
def get_project(name):
    project_found = [
        project for project in hint_projects if project["name"] == name]
    if len(project_found) > 0:
        return jsonify(project_found)
    return jsonify({"message": "Not Found"})
