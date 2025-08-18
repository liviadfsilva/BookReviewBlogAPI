from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.tag import Tag

class TagSchema(SQLAlchemyAutoSchema):
    id = fields.Int()
    name = fields.Str()
    
    class Meta:
        model = Tag