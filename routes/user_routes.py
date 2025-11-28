from flask import Blueprint, request, jsonify
from controllers.user_controller import (
    create_user, get_all_users, get_user_by_id,
    update_user, delete_user
)

user_bp = Blueprint("users", __name__)

def serialize(obj):
    if obj is None:
        return None
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

@user_bp.route("/", methods=["POST"])
def create():
    data = request.json
    u = create_user(data)
    return jsonify(serialize(u)), 201

@user_bp.route("/", methods=["GET"])
def all_users():
    users = get_all_users()
    return jsonify([serialize(u) for u in users])

@user_bp.route("/<int:user_id>", methods=["GET"])
def one(user_id):
    u = get_user_by_id(user_id)
    if not u:
        return jsonify({"message": "User not found"}), 404
    return jsonify(serialize(u))

@user_bp.route("/<int:user_id>", methods=["PUT"])
def update(user_id):
    u = update_user(user_id, request.json)
    if not u:
        return jsonify({"message": "User not found"}), 404
    return jsonify(serialize(u))

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete(user_id):
    ok = delete_user(user_id)
    if not ok:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"message": "User deleted"})
