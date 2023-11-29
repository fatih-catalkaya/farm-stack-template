from datetime import datetime

from beanie import PydanticObjectId
from fastapi import APIRouter, Response, HTTPException
from starlette import status

from app.model.TodoItem import TodoItem, CreateTodoItem, UpdateTodoItem

router = APIRouter(prefix="/todo")


@router.get("/")
async def get_todos() -> list[TodoItem]:
    return await TodoItem.find_all().to_list()


@router.get("/{id}")
async def get_todo(id: PydanticObjectId) -> TodoItem:
    return await TodoItem.get(id)


@router.post("/")
async def create_todo(body: CreateTodoItem, response: Response):
    if body.created_at is None:
        body.created_at = datetime.now()
    db_item = TodoItem(**body.model_dump())
    await db_item.create()
    response.status_code = status.HTTP_201_CREATED


@router.put("/{id}")
async def update_todo(id: PydanticObjectId, body: UpdateTodoItem, response: Response):
    req = {k: v for k, v in body.model_dump().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}
    todo_item = await TodoItem.get(id)
    if not todo_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo item not found!"
        )
    await todo_item.update(update_query)
    response.status_code = status.HTTP_201_CREATED


@router.delete("/{id}")
async def delete_todo(id: PydanticObjectId, response: Response):
    todo_item = await TodoItem.get(id)
    if not todo_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo item not found!"
        )
    await todo_item.delete()
    response.status_code = status.HTTP_201_CREATED
