from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.post import BlogPost

class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BlogPost
        include_fk = True