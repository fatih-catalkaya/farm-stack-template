from datetime import datetime
from typing import Optional

from beanie import Document
from pydantic import BaseModel


class TodoItem(Document):
    content: str
    created_at: datetime

    class Settings:
        name = "todo"


class CreateTodoItem(BaseModel):
    content: str
    created_at: Optional[datetime] = None


class UpdateTodoItem(BaseModel):
    content: Optional[str] = None
    created_at: Optional[datetime] = None
