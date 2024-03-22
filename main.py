from fastapi import FastAPI

from Controllers import authentication_route, task_route

app = FastAPI()

app.include_router(authentication_route.router, prefix="/api/auth")