from .db import db
from .base import Base
from sqlalchemy.orm import relationship
from .review_tags import book_review_tags

class Tag(Base):
    __tablename__ = "tags"
    
    name = db.Column(db.String(250), nullable=False, unique=True)
    
    book_reviews = relationship("BookReview", secondary=book_review_tags, back_populates="tags")