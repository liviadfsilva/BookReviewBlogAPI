from .db import db

book_review_tags = db.Table(
    "book_reviews_tags",
    db.Column("book_review_id", db.Integer, db.ForeignKey("book_reviews.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True)
)