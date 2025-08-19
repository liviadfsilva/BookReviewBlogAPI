from .db import db
from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .review_tags import book_review_tags

class BookReview(Base):
    __tablename__ = "book_reviews"
    
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    cover_url = db.Column(db.String(2083), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    spice_rating = db.Column(db.Integer)
    slug = db.Column(db.String, nullable=False, unique=True)
    
    user_id = db.Column(ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="reviews")
    
    tags = relationship("Tag", secondary=book_review_tags, back_populates="book_reviews")