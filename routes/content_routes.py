from flask import Blueprint, request, jsonify
from controllers.content_controller import (
    create_content, get_all_contents, get_content_by_id,
    update_content, delete_content
)

content_bp = Blueprint("contents", __name__)

def serialize(obj):
    if obj is None:
        return None
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

@content_bp.route("/", methods=["POST"])
def create():
    c = create_content(request.json)
    return jsonify(serialize(c)), 201

@content_bp.route("/", methods=["GET"])
def all_contents():
    items = get_all_contents()
    return jsonify([serialize(x) for x in items])

@content_bp.route("/<int:content_id>", methods=["GET"])
def one(content_id):
    c = get_content_by_id(content_id)
    if not c:
        return jsonify({"message": "Content not found"}), 404
    return jsonify(serialize(c))

@content_bp.route("/<int:content_id>", methods=["PUT"])
def update(content_id):
    c = update_content(content_id, request.json)
    if not c:
        return jsonify({"message": "Content not found"}), 404
    return jsonify(serialize(c))

@content_bp.route("/<int:content_id>", methods=["DELETE"])
def delete(content_id):
    ok = delete_content(content_id)
    if not ok:
        return jsonify({"message": "Content not found"}), 404
    return jsonify({"message": "Content deleted"})
