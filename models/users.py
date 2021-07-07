from tortoise import fields, models 
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseModel


class User(BaseModel):
    username = fields.CharField(max_length=100, required=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=200, null=True)
    is_admin = fields.BooleanField(default=False)

class UserProfile(BaseModel):
    user_id = fields.ForeignKeyField('models.User', related_name="profile")
    full_name = fields.CharField(max_length=100, null=True)
    phone = fields.CharField(max_length=100, null=True)
    bio = fields.CharField(max_length=200, null=True)


UserPydantic = pydantic_model_creator(
    User,
    name="User",
    include=(
        "id",
        "email",
        "username"
    )
)

UserInPydantic = pydantic_model_creator(
    User,
    name="UserIn",
    include=(
        "username",
        "email",
        "password",
    )
)