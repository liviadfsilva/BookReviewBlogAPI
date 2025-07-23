from app.models.db import db
from app.models.tag import Tag

def seed_tags():
    tags = [
        Tag(name="Adventure"),
        Tag(name="Children's"),
        Tag(name="Contemporary"),
        Tag(name="Dark Romance"),
        Tag(name="Drama"),
        Tag(name="Erotica"),
        Tag(name="Fantasy"),
        Tag(name="Graphic Novel"),
        Tag(name="Historical"),
        Tag(name="Horror"),
        Tag(name="Mystery"),
        Tag(name="Nonfiction"),
        Tag(name="Poetry"),
        Tag(name="Romance"),
        Tag(name="Science Fiction"),
        Tag(name="Spirituality"),
        Tag(name="Thriller"),
        Tag(name="Young Adult")
    ]
    
    db.session.add_all(tags)
    db.session.commit()