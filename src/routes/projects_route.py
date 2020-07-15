from flask import Blueprint, jsonify
import requests

projects_bp = Blueprint('projects_bp', __name__)

projects = requests.get('https://api.github.com/orgs/Hint-Box/repos')


@projects_bp.route('/projects')
def get_projects():
    hintbox_projects = [pro for pro in projects.json()]
    return jsonify(hintbox_projects)
