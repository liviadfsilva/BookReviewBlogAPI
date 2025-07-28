from .db import db
from .base import Base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):
    __tablename__ = "users"
    
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password_hash = db.Column(db.String(250), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
                    
    reviews = relationship("BookReview", back_populates="user")
    posts = relationship("BlogPost", back_populates="user")