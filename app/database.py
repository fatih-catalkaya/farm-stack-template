import motor.motor_asyncio
from beanie import init_beanie

from app.model.TodoItem import TodoItem
from app.setting import settings


async def initialize_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASS}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DB}"
    )
    await init_beanie(database=client[settings.MONGO_DB], document_models=[TodoItem])
