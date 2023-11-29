from fastapi import FastAPI
from app.controller.todo_controller import router as todo_controller_router
from app.database import initialize_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await initialize_db()


app.include_router(todo_controller_router)
