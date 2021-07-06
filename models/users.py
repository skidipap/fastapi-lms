from tortoise import fields, models 
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseModel


class User(BaseModel):
    username = fields.CharField(max_length=100, required=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=200, null=True)
    is_active = fields.BooleanField(default=False)


UserPydantic = pydantic_model_creator(
    User,
    name="User",
    include=(
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