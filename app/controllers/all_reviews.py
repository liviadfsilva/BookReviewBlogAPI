from flask import Blueprint, jsonify

all_reviews = Blueprint("all_reviews", __name__)

@all_reviews.route("/", methods=["GET"])
def all_reviews_page():
    return jsonify(response={"success": "Successfully accessed All Reviews page."}), 200