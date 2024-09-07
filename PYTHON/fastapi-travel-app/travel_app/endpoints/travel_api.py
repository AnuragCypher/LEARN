from typing import Annotated, List
from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from fastapi.security import OAuth2PasswordRequestForm
from travel_app.core.utils import create_access_token, get_current_user
from travel_app.database.mongodb import User, UserPreferences, db_connection


route = APIRouter()


@route.get("/health_check")
async def health_check():
    return "application is up"


@route.post("/create_user")
async def create_user(user: User = Body(...), db=Depends(db_connection)):
    user_data = dict(user)
    new_user = User(**user_data)
    await new_user.create()
    return new_user


@route.post("/token")
async def get_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db=Depends(db_connection),
):
    user = {"username": form_data.username, "password": form_data.password}
    user_check = await User.find_one(User.username == form_data.username)
    if not user_check:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        access_token = await create_access_token(
            user={
                "username": user["username"],
                "password": user["password"],
                "role": user_check.role.value,
            }
        )
        return {"access_token": access_token, "token_type": "bearer"}


@route.post("/set_prefrence")
async def set_prefrence(
    user=Depends(get_current_user),
    prefrecces: List[UserPreferences] = Body(...),
    db=Depends(db_connection),
):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", user)
    if user["role"] == "admin":
        return prefrecces
    else:
        raise HTTPException(status_code=401, detail="unauthorized")
