from fastapi import APIRouter, HTTPException
from typing import List 

import models 


tags = ["user"]
router = APIRouter(
    prefix='/user',
    tags=tags,
)

@router.post("/", response_model=models.UserPydantic)
async def create_user(form_data: models.UserInPydantic):
    obj_user = await models.User.create(**form_data.dict(exclude_unset=True))

    return await models.UserPydantic.from_tortoise_orm(obj_user)

@router.get("/", response_model=List[models.UserPydantic])
async def get_user():
    obj_user = await models.User.all()

    return await models.UserPydantic.from_queryset(obj_user)

@router.get("/{user_id}", response_model=models.UserPydantic)
async def get_user_by_id(user_id: int):
    obj_user = await models.User.filter(id=user_id).first()

    return await models.UserPydantic.from_tortoise_orm(obj_user)

@router.put("/{user_id}")

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    obj_user = await models.User.filter(id=user_id).delete()

    if not obj_user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    
    return {
        "detail" : f"Deleted user {user_id}"
    }