from beanie import Document
from typing import List, Optional
from pydantic import HttpUrl, Field
from datetime import datetime


class ItemTag(Document):
    name: str
    description: Optional[str] = None


class ItemImage(Document):
    url: HttpUrl
    name: str


class Item(Document):
    name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = Field(None, min_length=10, max_length=300)
    price: float = Field(..., gt=0)
    tax: Optional[float] = Field(None, ge=0)
    tags: List[ItemTag] = []
    images: Optional[List[ItemImage]] = Field(None, min_items=1)
    created_at: datetime = Field(default_factory=datetime.utcnow)
