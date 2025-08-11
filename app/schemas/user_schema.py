from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.user import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        fields = ("id", "name", "email")