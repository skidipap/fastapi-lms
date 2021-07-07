from datetime import datetime, timedelta 
import uuid

import jwt 
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from config.auth import ACCESS_TOKEN_EXPIRE_MINUTES, AUTH_SECRET_KEY, ALGORITHM

import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def login_with_password(email: str, password: str):
    user = await models.User.get_active_user(email=email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTP_401_UNAUTHORIZED
    return user