from tortoise import fields, models 
from tortoise.contrib.pydantic import pydantic_model_creator

import uuid

from .base import BaseModel
from services import auth


class User(BaseModel):
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=200, null=True)
    username = fields.CharField(max_length=100, required=True)
    is_admin = fields.BooleanField(default=False)

    @classmethod
    async def get_active_user(cls, user_id: int = None, email: str = None):
        if user_id is not None:
            return await cls.get_or_none(id=user_id, deleted_at=None)
        if email is not None:
            return await cls.get_or_none(email=email, deleted_at=None)
        return None

    @classmethod
    def update(cls, **kwargs):
        kwargs["password"] = auth.get_password_hash(kwargs["password"])
        return super().update(**kwargs)


    @classmethod
    def create(cls, **kwargs):
        kwargs["password"] = auth.get_password_hash(kwargs["password"])
        return super().create(**kwargs)
    

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