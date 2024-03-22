from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class Task(BaseModel):
    id: int | None
    username: str
    description: str
    status: bool
