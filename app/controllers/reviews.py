from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.review import BookReview
from app.models.db import db
from app.models.tag import Tag

reviews = Blueprint("reviews", __name__)

@reviews.route("/", methods=["GET"])
def get_reviews():
    reviews = BookReview.query.all()
    
    if not reviews:
        return jsonify({"error": "No reviews found."}), 404
    
    return jsonify(response={"success": "Successfully accessed reviews."}), 200

@reviews.route("/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = BookReview.query.get_or_404(review_id)
    
    return jsonify(review)

@reviews.route("/", methods=["POST"])
@jwt_required()
def create_review():
    data = request.get_json()
    current_user_id = int(get_jwt_identity())
    
    title = data.get("title")
    author = data.get("author")
    cover_url = data.get("cover_url")
    review = data.get("review")
    rating = data.get("rating")
    spice_rating = data.get("spice_rating")
    tag_ids = data.get("tag_ids")
    
    if not title or not author or not cover_url or not review or not rating or not tag_ids:
        return jsonify({"error": "Title, Author, Cover_URL, Reviews, Rating and Tag_IDs are required."}), 400
    
    if BookReview.query.filter_by(title=title).first():
        return jsonify({"error": "There's already a review with this title."}), 400
    
    tags = []
    for tag_id in tag_ids:
        tag = db.session.get(Tag, tag_id)
        if not tag:
            return jsonify({"error": f"Tag with id {tag_id} not found."}), 404
        tags.append(tag)
    
    new_review = BookReview(
        title=title,
        author=author,
        cover_url=cover_url,
        review=review,
        rating=rating,
        spice_rating=spice_rating,
        tags=tags,
        user_id=current_user_id
    )
    
    db.session.add(new_review)
    db.session.commit()
    
    return jsonify({"success": "Review created successfully."}), 201

@reviews.route("/<int:review_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_review(review_id):
    current_user_id = int(get_jwt_identity())
    book_review = BookReview.query.get_or_404(review_id)
    
    if book_review.user_id != current_user_id:
        return jsonify({"error": "You do not have permission to modify this review."}), 403
    
    data = request.get_json()
    
    if "title" in data:
        existing = BookReview.query.filter_by(title=data["title"]).first()
        if existing and existing.id != book_review.id:
            return jsonify({"error": "There's already a review with this title."}), 400
        book_review.title = data["title"]
        
    if request.method == "PUT":
        required_fields = ["title", "author", "cover_url", "review", "rating", "tag_ids"]
        missing = [field for field in required_fields if field not in data or data[field] is None]
        
        if missing:
            return jsonify({"error": f"Missing required fields for full update: {', '.join(missing)}"}), 400
        
        book_review.title = data["title"]
        book_review.author = data["author"]
        book_review.cover_url = data["cover_url"]
        book_review.review = data["review"]
        book_review.rating = data["rating"]
        book_review.spice_rating = data.get("spice_rating")
        
        tag_ids = data["tag_ids"]
        if not isinstance(tag_ids, list) or len(tag_ids) == 0:
            return jsonify({"error": "tag_ids must be a non-empty list."}), 400
        
        tags = []
        for tag_id in tag_ids:
            tag = db.session.get(Tag, tag_id)
            if not tag:
                return jsonify({"error": f"Tag with id {tag_id} not found."}), 404
            tags.append(tag)
        book_review.tags = tags
    
    else:
        if "author" in data:
            book_review.author = data["author"]
        if "cover_url" in data:
            book_review.cover_url = data["cover_url"]
        if "review" in data:
            book_review.review = data["review"]
        if "rating" in data:
            book_review.rating = data["rating"]
        if "spice_rating" in data:
            book_review.spice_rating = data["spice_rating"]
            
        if "tag_ids" in data:
            tag_ids = data["tag_ids"]
            if not isinstance(tag_ids, list) or len(tag_ids) == 0:
                return jsonify({"error": "tag_ids must be a non-empty list."}), 400
            
            tags = []
            for tag_id in tag_ids:
                tag = db.session.get(Tag, tag_id)
                if not tag:
                    return jsonify({"error": f"Tag with id {tag_id} not found."}), 404
                tags.append(tag)
            book_review.tags = tags
        
    db.session.commit()
    
    return jsonify({"success": "Review updated successfully."}), 200

@reviews.route("/<int:review_id>", methods=["DELETE"])
@jwt_required()
def delete_review(review_id):
    current_user_id = int(get_jwt_identity())
    book_review = BookReview.query.get_or_404(review_id)
    
    if book_review.user_id != current_user_id:
        return jsonify({"error": "You do not have permission to delete this review."}), 403
    
    db.session.delete(book_review)
    db.session.commit()
    
    return jsonify({"success": "Review deleted successfully."})
        
    
    