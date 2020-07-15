from flask import Blueprint, jsonify
import requests


projects_bp = Blueprint('projects_bp', __name__)

projects = requests.get('https://api.github.com/orgs/Hint-Box/repos')


@projects_bp.route('/projects')
def get_projects():
    hintbox_projects = [pro for pro in projects.json()]
    hint_json = [{
        "id": hintbox_projects[0]["id"],
        "name": hintbox_projects[0]["name"],
        "url": hintbox_projects[0]["url"],
        "githubURL": hintbox_projects[0]["html_url"],
        "created_at": hintbox_projects[0]["created_at"],
        "description": hintbox_projects[0]["description"],
        "tags": requests.get('https://api.github.com/repos/Hint-Box/HintBoxAPI/tags').json(),
        "collaborators": requests.get('https://api.github.com/repos/Hint-Box/HintBoxAPI/collaborators').json(),
        "contributors": requests.get('https://api.github.com/repos/Hint-Box/HintBoxAPI/contributors').json()
    }]
    return jsonify(hint_json)


@projects_bp.route('/projects/<string:name>')
def get_project(name):
    return jsonify({"project": name})
