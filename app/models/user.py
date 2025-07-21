from .db import db
from .base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password_hash = db.Column(db.String(250), nullable=False)
    
    reviews = relationship("BookReview", back_populates="user")
    posts = relationship("BlogPost", back_populates="user")