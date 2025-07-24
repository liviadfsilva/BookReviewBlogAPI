from flask import Blueprint, jsonify
from app.models.review import BookReview

reviews = Blueprint("reviews", __name__)

@reviews.route("/", methods=["GET"])
def get_reviews():
    reviews = BookReview.query.all()
    
    if not reviews:
        return jsonify({"error": "No reviews found."}), 404
    
    return jsonify(response={"success": "Successfully accessed reviews."}), 200