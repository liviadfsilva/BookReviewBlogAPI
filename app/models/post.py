from .db import db
from .base import Base

class BlogPost(Base):
    __tablename__ = "posts"
    
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    musing = db.Column(db.Text, nullable=False)