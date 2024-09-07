from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import Field
from my_app.models.models import Item, ItemImage, ItemTag
from beanie import Document, init_beanie
from typing import Generator


class UserMongo(Document):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)


async def db_connection() -> Generator:  # type: ignore
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.travel_app, document_models=[UserMongo])
    yield
