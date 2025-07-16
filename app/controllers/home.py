from flask import Blueprint, jsonify

home = Blueprint("home", __name__)

@home.route ("/", methods=["GET"])
def home_page():
    return jsonify(response={"success": "Successfully accessed the home page."}), 200