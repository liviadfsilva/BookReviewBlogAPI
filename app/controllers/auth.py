from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from app.initializer import jwt
from app.models.user import User
from datetime import timedelta

auth = Blueprint("auth", __name__)

revoked_token = set()

def add_token_to_revoked_list(jti):
    revoked_token.add(jti)
    
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in revoked_token

@auth.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided."}), 400
        
        email = data.get("email")
        password = data.get("password")
        
        if not email or not password:
            return jsonify({"error": "Both email and password are required."}), 400
        
        user = User.query.filter_by(email=email).first()
        if not user or not user.verify_password(password):
            return jsonify({"error": "Invalid email or password."}), 400
        if not user.is_active:
            return jsonify({"error": "This user is not active."}), 400
        
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(hours=12))
        
        first_name = user.name.split()[0]
        
        return jsonify({
            "token": token,
            "exp": timedelta(hours=12).total_seconds(),
            "name": first_name
        }), 200
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@auth.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    add_token_to_revoked_list(jti)
    return jsonify({'msg': 'Logout successfully completed'}), 200