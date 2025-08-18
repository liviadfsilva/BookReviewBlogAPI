from flask import Blueprint, jsonify
from app.models.tag import Tag
from app.schemas import TagSchema

tags = Blueprint("tags", __name__)

@tags.route("/", methods=["GET"])
def get_tags():
    tags = Tag.query.all()
    if not tags:
        return jsonify({"error": "No tags found"}), 404

    return jsonify(TagSchema(many=True).dump(tags)), 200