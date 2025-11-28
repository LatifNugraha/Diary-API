from flask import Blueprint, request, jsonify
from controllers.diary_controller import (
    create_entry, get_all_entries, get_entry_by_id,
    update_entry, delete_entry
)

diary_bp = Blueprint("diary", __name__)

def serialize_entry(obj):
    if obj is None:
        return None
    data = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
    data["tag_ids"] = [t.id for t in obj.tags]
    data["tags"] = [{"id": t.id, "name": t.name} for t in obj.tags]
    return data

@diary_bp.route("/", methods=["POST"])
def create():
    payload = request.json
    entry = create_entry(payload)
    return jsonify(serialize_entry(entry)), 201

@diary_bp.route("/", methods=["GET"])
def all_entries():
    items = get_all_entries()
    return jsonify([serialize_entry(e) for e in items])

@diary_bp.route("/<int:entry_id>", methods=["GET"])
def one(entry_id):
    e = get_entry_by_id(entry_id)
    if not e:
        return jsonify({"message": "Entry not found"}), 404
    return jsonify(serialize_entry(e))

@diary_bp.route("/<int:entry_id>", methods=["PUT"])
def update(entry_id):
    e = update_entry(entry_id, request.json)
    if not e:
        return jsonify({"message": "Entry not found"}), 404
    return jsonify(serialize_entry(e))

@diary_bp.route("/<int:entry_id>", methods=["DELETE"])
def delete(entry_id):
    ok = delete_entry(entry_id)
    if not ok:
        return jsonify({"message": "Entry not found"}), 404
    return jsonify({"message": "Entry deleted"})
