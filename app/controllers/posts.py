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

@posts.route("/", methods=["POST"])
@jwt_required()
def create_post():
    data = request.json()
    current_user_id = int(get_jwt_identity)
    
    title = data.get("title")
    subtitle = data.get("subtitle")
    musing = data.get("musing")
    
    if not title or not subtitle or not musing:
        return jsonify({"error": "Title, subtitle and musing are required."}), 400
    
    if BlogPost.query.filter_by(title=title).first():
        return jsonify({"error": "There's already a musing with this title."}), 400
    
    new_blog_post = BlogPost(
        title=title,
        subtitle=subtitle,
        musing=musing,
        user_id=current_user_id
    )
    
    db.session.add(new_blog_post)
    db.session.commit()
    
    return jsonify({"success": "Blog post created successfully."}), 201
    
@posts.route("/", methods=["PUT", "PATCH"])
@jwt_required()
def update_post():
    pass

@posts.route("/", methods=["DELETE"])
@jwt_required()
def delete_post():
    pass