from flask import Blueprint, request, jsonify
from controllers.tag_controller import (
    create_tag, get_all_tags, get_tag_by_id,
    update_tag, delete_tag
)

tag_bp = Blueprint("tags", __name__)

def serialize(obj):
    if obj is None:
        return None
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

@tag_bp.route("/", methods=["POST"])
def create():
    t = create_tag(request.json)
    return jsonify(serialize(t)), 201

@tag_bp.route("/", methods=["GET"])
def all_tags():
    ts = get_all_tags()
    return jsonify([serialize(x) for x in ts])

@tag_bp.route("/<int:tag_id>", methods=["GET"])
def one(tag_id):
    t = get_tag_by_id(tag_id)
    if not t:
        return jsonify({"message": "Tag not found"}), 404
    return jsonify(serialize(t))

@tag_bp.route("/<int:tag_id>", methods=["PUT"])
def update(tag_id):
    t = update_tag(tag_id, request.json)
    if not t:
        return jsonify({"message": "Tag not found"}), 404
    return jsonify(serialize(t))

@tag_bp.route("/<int:tag_id>", methods=["DELETE"])
def delete(tag_id):
    ok = delete_tag(tag_id)
    if not ok:
        return jsonify({"message": "Tag not found"}), 404
    return jsonify({"message": "Tag deleted"})
