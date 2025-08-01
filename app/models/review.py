from .db import db
from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class BookReview(Base):
    __tablename__ = "book_reviews"
    
    title = db.Column(db.String(250), nullable=False, unique=True)
    cover_url = db.Column(db.String(2083), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    spice_rating = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="reviews")
    
    tag_id = db.Column(ForeignKey("tags.id"), nullable=False)
    tag = relationship("Tag", back_populates="books")