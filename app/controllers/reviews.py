from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.review import BookReview
from app.models.db import db
from app.models.tag import Tag
from app.schemas import ReviewSchema
from slugify import slugify

reviews = Blueprint("reviews", __name__)

@reviews.route("/", methods=["GET"])
def get_reviews():
    reviews = BookReview.query.all()
    
    reviews_data = []
    for review in reviews:
        review_dict = ReviewSchema().dump(review)
        review_dict["tag_names"] = [tag.name for tag in review.tags]
        reviews_data.append(review_dict)
    
    if not reviews:
        return jsonify({"error": "No reviews found."}), 404
    
    return jsonify(reviews_data), 200

@reviews.route("/<slug>", methods=["GET"])
def get_review(slug):
    review = BookReview.query.filter_by(slug=slug).first_or_404()
    review_data = ReviewSchema().dump(review)
    
    review_data["tag_names"] = [tag.name for tag in review.tags]

    return jsonify(review_data)

@reviews.route("/latest", methods=["GET"])
def get_latest_reviews():
    reviews = BookReview.query.order_by(BookReview.id.desc()).limit(3).all()
    return jsonify(ReviewSchema(many=True).dump(reviews))

@reviews.route("/category/<string:category_name>", methods=["GET"])
def get_reviews_by_category(category_name):
    category_name = category_name.replace("-", " ")
    reviews = BookReview.query.join(BookReview.tags).filter(Tag.name.ilike(category_name)).all()
    
    reviews_data = []
    for review in reviews:
        review_dict = ReviewSchema().dump(review)
        review_dict["tag_names"] = [tag.name for tag in review.tags]
        reviews_data.append(review_dict)

    if not reviews:
        return jsonify({"error": f"No reviews found for category '{category_name}'"}), 404

    return jsonify(reviews_data), 200

@reviews.route("/five-star-reviews", methods=["GET"])
def get_five_star_reviews():
    reviews = BookReview.query.filter_by(rating=5).all()

    reviews_data = []
    for review in reviews:
        review_dict = ReviewSchema().dump(review)
        review_dict["tag_names"] = [tag.name for tag in review.tags]
        reviews_data.append(review_dict)

    if not reviews:
        return jsonify({"error": "No five-star reviews found"}), 404

    return jsonify(reviews_data), 200

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
    
    if title is None or author is None or cover_url is None or review is None or rating is None or tag_ids is None:
        return jsonify({"error": "Title, Author, Cover_URL, Review, Rating and Tag_IDs are required."}), 400
    
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
        user_id=current_user_id,
        slug=slugify(data["title"])
    )
    
    db.session.add(new_review)
    db.session.commit()
    
    new_review_result = ReviewSchema().dump(new_review)
    new_review_result["tag_names"] = [tag.name for tag in new_review.tags]
    
    return jsonify({"new_review": new_review_result}), 201

@reviews.route("/<slug>", methods=["PUT", "PATCH"])
@jwt_required()
def update_review(slug):
    current_user_id = int(get_jwt_identity())
    book_review = BookReview.query.filter_by(slug=slug).first_or_404()
    
    if book_review.user_id != current_user_id:
        return jsonify({"error": "You do not have permission to modify this review."}), 403
    
    data = request.get_json()
    
    if "title" in data:
        existing = BookReview.query.filter_by(title=data["title"]).first()
        if existing and existing.id != book_review.id:
            return jsonify({"error": "There's already a review with this title."}), 400
        book_review.title = data["title"]
        book_review.slug = slugify(data["title"])
        
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
    updated_review = ReviewSchema().dump(book_review)
    updated_review["tag_names"] = [tag.name for tag in book_review.tags]
    
    return jsonify({"updated_review": updated_review}), 200

@reviews.route("/<slug>", methods=["DELETE"])
@jwt_required()
def delete_review(slug):
    current_user_id = int(get_jwt_identity())
    book_review = BookReview.query.filter_by(slug=slug).first_or_404()
    
    if book_review.user_id != current_user_id:
        return jsonify({"error": "You do not have permission to delete this review."}), 403
    
    db.session.delete(book_review)
    db.session.commit()
    
    return jsonify({"msg": "Review deleted successfully."})
        
    
    