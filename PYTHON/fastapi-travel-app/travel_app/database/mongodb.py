from datetime import datetime
from enum import Enum
from beanie import Document, init_beanie
from pydantic import BaseModel, Field
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Generator, Optional


class Role(Enum):
    ADMIN = "admin"
    USER = "user"


class User(Document):
    username: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    role: Role = Field(...)


class Budget(BaseModel):
    min: int = Field(..., example=500, description="Minimum budget for travel in USD.")
    max: int = Field(..., example=1500, description="Maximum budget for travel in USD.")


class Preferences(BaseModel):
    weather: str = Field(
        ..., example="warm", description="Preferred weather condition."
    )
    budget: Budget = Field(..., description="Budget range for travel.")
    season: str = Field(..., example="summer", description="Preferred travel season.")


class UserPreferences(Document):
    id: Optional[str] = Field(
        None, alias="_id", description="Unique identifier for the user."
    )
    username: str = Field(
        ..., example="traveler_john_doe", description="Username of the user."
    )
    preferences: Preferences = Field(..., description="User's travel preferences.")
    createdAt: Optional[datetime] = Field(
        default_factory=datetime.now,
        description="Timestamp of when the user preference was created.",
    )
    updatedAt: Optional[datetime] = Field(
        default_factory=datetime.now,
        description="Timestamp of the last update to the user preference.",
    )


async def db_connection() -> Generator:  # type: ignore
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(
        database=client.travel_app, document_models=[User, UserPreferences]
    )
    yield
