from my_app.database import db_initialize


async def create_table():
    async with db_initialize.engine.begin() as conn:
        # await conn.run_sync(db_initialize.Base.metadata.drop_all)
        await conn.run_sync(db_initialize.Base.metadata.create_all)


import asyncio
from sqlalchemy import Column, Integer, String


class User(db_initialize.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


# asyncio.run(create_table())
