from fastapi import APIRouter, Response, Request, status
from jwt_util import decode_jwt

from Entities.request_body_entities import User, Task
from DAO.task_dao import get_tasks, create_task, get_task, update_task_description, update_task_status, delete_task

router = APIRouter()


@router.get("/", status_code=200)
async def get_all_tasks(request: Request, response: Response):
    token = request.headers.get("Authorization")
    if token is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Token not found"}

    user = decode_jwt(token.split(" ")[1].strip())
    if user is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Invalid token"}

    tasks = get_tasks(user["username"])
    return tasks


@router.get("/{task_id}", status_code=200)
async def get_task_by_id(request: Request, response: Response, task_id: int):
    token = request.headers.get("Authorization")
    if token is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Token not found"}

    user = decode_jwt(token.split(" ")[1].strip())
    if user is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Invalid token"}

    task = get_task(user["username"], task_id)
    if task is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Task not found"}

    return task


@router.post("/", status_code=201)
async def create_new_task(request: Request, response: Response, task: Task):
    token = request.headers.get("Authorization")
    if token is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Token not found"}

    user = decode_jwt(token.split(" ")[1].strip())
    if user is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Invalid token"}

    create_task(user["username"], task.description)
    return {"message": "Task created"}


@router.put("/update_description/{task_id}", status_code=200)
async def update_task_description_by_id(request: Request, response: Response, task_id: int, task: Task):
    token = request.headers.get("Authorization")
    if token is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Token not found"}

    user = decode_jwt(token.split(" ")[1].strip())
    if user is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Invalid token"}

    task_data = get_task(user["username"], task_id)
    if task_data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Task not found"}

    update_task_description(user["username"], task_id, task.description)
    return {"message": "Task description updated"}


@router.put("/update_status/{task_id}", status_code=200)
async def update_task_status_by_id(request: Request, response: Response, task_id: int, task: Task):
    token = request.headers.get("Authorization")
    if token is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Token not found"}

    user = decode_jwt(token.split(" ")[1].strip())
    if user is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Invalid token"}

    task_data = get_task(user["username"], task_id)
    if task_data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Task not found"}

    update_task_status(user["username"], task_id, task.status)
    return {"message": "Task status updated"}


@router.delete("/{task_id}", status_code=200)
async def delete_task_by_id(request: Request, response: Response, task_id: int):
    token = request.headers.get("Authorization")
    if token is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Token not found"}

    user = decode_jwt(token.split(" ")[1].strip())
    if user is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Invalid token"}

    task_data = get_task(user["username"], task_id)
    if task_data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Task not found"}

    delete_task(user["username"], task_id)
    return {"message": "Task deleted"}