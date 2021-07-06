from fastapi import APIRouter 
from typing import List 

import models 


tags = ["user"]
router = APIRouter()

@router.post("/users", tags=tags, response_model=models.UserPydantic)
async def create_user(form_data: models.UserInPydantic):
    obj_user = await models.User.create(**form_data.dict(exclude_unset=True))

    return await models.UserPydantic.from_tortoise_orm(obj_user)

@router.get("/users", tags=tags, response_model=List[models.UserPydantic])
async def get_user():
    return await models.UserPydantic.from_queryset(models.User.all())