from flask import Blueprint, jsonify

reviews = Blueprint("reviews", __name__)

@reviews.route("/", methods=["GET"])
def all_reviews():
    return jsonify(response={"success": "Successfully accessed All Reviews page."}), 200