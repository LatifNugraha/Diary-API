from flask import Blueprint, request, jsonify
from controllers.mood_controller import (
    create_mood, get_all_moods, get_mood_by_id,
    update_mood, delete_mood
)

mood_bp = Blueprint("moods", __name__)

def serialize(obj):
    if obj is None:
        return None
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

@mood_bp.route("/", methods=["POST"])
def create():
    m = create_mood(request.json)
    return jsonify(serialize(m)), 201

@mood_bp.route("/", methods=["GET"])
def all_moods():
    ms = get_all_moods()
    return jsonify([serialize(x) for x in ms])

@mood_bp.route("/<int:mood_id>", methods=["GET"])
def one(mood_id):
    m = get_mood_by_id(mood_id)
    if not m:
        return jsonify({"message": "Mood not found"}), 404
    return jsonify(serialize(m))

@mood_bp.route("/<int:mood_id>", methods=["PUT"])
def update(mood_id):
    m = update_mood(mood_id, request.json)
    if not m:
        return jsonify({"message": "Mood not found"}), 404
    return jsonify(serialize(m))

@mood_bp.route("/<int:mood_id>", methods=["DELETE"])
def delete(mood_id):
    ok = delete_mood(mood_id)
    if not ok:
        return jsonify({"message": "Mood not found"}), 404
    return jsonify({"message": "Mood deleted"})
