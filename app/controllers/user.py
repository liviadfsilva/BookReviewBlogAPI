from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.models.user import User
from app.models.db import db
from app.controllers.auth import add_token_to_revoked_list

user = Blueprint("user", __name__)

@user.route("/", methods=["GET"])
def get_users():
    pass

@user.route("/", methods=["POST"])
@jwt_required()
def create_user():
    data = request.get_json()
    
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    confirm_password = data.get("confirm_password")
    
    if not name or not email or not password or not confirm_password:
        return jsonify({'error': 'Name, email, password, and password confirmation are required'}), 400

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email is already in use'}), 400

    user = User(name=name, email=email)
    user.password = password
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"success": "User created successfully."}), 201

@user.route("/", methods=["PUT", "PATCH"])
def edit_user():
    pass

@user.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    current_user_id = int(get_jwt_identity())
    user = User.query.get_or_404(id)
    
    if user.id != current_user_id:
        return jsonify({"error": "You do not have permission to delete this user"}), 403

    user.is_active = False
    db.session.commit()
    
    jti = get_jwt()['jti']
    add_token_to_revoked_list(jti)
    
    return jsonify({'msg': 'User successfully deleted'}), 200