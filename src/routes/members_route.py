from flask import Blueprint, jsonify
from src.models.members import members

members_bp = Blueprint("members_bp", __name__)


@members_bp.route("/members", methods=["GET"])
def get_members():
    return jsonify(members)


@members_bp.route("/members/<string:name>", methods=["GET"])
def get_member(name):
    member_found = [
        member for member in members if member["login"] == name]
    if len(member_found) > 0:
        return jsonify(member_found)
    return jsonify({"message": "Not Found"})
