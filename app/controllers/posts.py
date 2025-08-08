from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.post import BlogPost
from app.models.db import db

posts = Blueprint("posts", __name__)

@posts.route("/", methods=["GET"])
@jwt_required()
def get_posts():
    blog_posts = BlogPost.query.all()
    
    if not blog_posts:
        return jsonify({"error": "No blog posts found."}), 404
    
    return jsonify({"success": "Sucessfully retrieved all posts."}), 200