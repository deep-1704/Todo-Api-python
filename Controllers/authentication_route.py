from fastapi import APIRouter, Response, status
from jwt_util import encode_jwt

from Entities.request_body_entities import User
from DAO.user_dao import get_user_by_username, create_user

router = APIRouter()


@router.post("/login", status_code=201)
async def login(user: User, response: Response):
    user_data = get_user_by_username(user.username)
    if user_data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "User not found"}
    if user_data["password"] != user.password:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Invalid password"}
    token = encode_jwt(user_data)
    return {"token": token}


@router.post("/register", status_code=201)
async def register(user: User, response: Response):
    user_data = get_user_by_username(user.username)
    if user_data is not None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "User already exists"}
    create_user(user.username, user.password)
    return {"message": "User created"}