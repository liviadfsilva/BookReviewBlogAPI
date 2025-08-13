from .db import db
from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class BlogPost(Base):
    __tablename__ = "posts"
    
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    post_img = db.Column(db.String(2083), nullable=True)
    musing = db.Column(db.Text, nullable=False)
    user_id = db.Column(ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="posts")