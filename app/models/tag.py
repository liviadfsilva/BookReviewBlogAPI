from .db import db
from .base import Base
from sqlalchemy.orm import relationship

class Tag(Base):
    __tablename__ = "tags"
    
    name = db.Column(db.String(250), nullable=False, unique=True)
    
    books = relationship("BookReview", back_populates="tag")