from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.review import BookReview

class ReviewSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BookReview
        include_fk = True