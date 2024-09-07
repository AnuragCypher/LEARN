from datetime import datetime, timedelta
from enum import Enum
from typing import Annotated, Generator, Optional
from fastapi import (
    APIRouter,
    Body,
    Cookie,
    Depends,
    File,
    Form,
    HTTPException,
    Path,
    Query,
    Request,
    UploadFile,
    status,
)
from fastapi.responses import JSONResponse
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
)
from pydantic import BaseModel, Field
from db_init import User
from mongo_db_document_create import UserMongo, db_connection
from my_app.database.db_initialize import SessionLocal
from my_app.models.models import Item as Item_
import main
import asyncio


route = APIRouter()


@route.get("/health_check")
async def health_check():
    await asyncio.sleep(600)
    return JSONResponse({"message": "application is up uppppppppppppppppp"})


# @route.get("/books/{type_of_var}")
# async def get_books(type_of_var: str):
#     return JSONResponse({"type of book": type})


# # below is how you can restrict and validtae the path parameters to have a defined set of values ..
# class State(str, Enum):
#     active = "active"
#     pending = "pending"
#     failed = "failed"


# @route.get("/check_state/{state}")
# async def state_check(state: State):
#     match state:
#         case state.active:
#             return JSONResponse({"message": "application is running"})

#         case state.pending:
#             return JSONResponse({"message": "application is in rest phase"})

#         case state.failed:
#             return JSONResponse({"message": "application is halted"})


# """when we pass function arguement to some endpoint without adding it into path stirng it automatically interpreted as query variable"""

# @route.get("/test_query_params")
# async def check_query_param(qd: str):
#     return JSONResponse({"got the query data": f"query data is {qd}"})


# """we can also add query param and path variable in smae route"""


# @route.get("/path_and_query_data/{path_data}")
# async def get_both(path_data: str, query_data: int = None):
#     return JSONResponse({"path_data": path_data, "query_data": query_data})


# """in above rouet the api route would look like this , http://0.0.0.0:8000/api/path_and_query_data/hello%20world?query_data=1 """
# """if we would query param not required we just declare it as None """


# """if we want to provide the meta data to path and query params we use Path for path variales and Query for query varibales"""

# @route.get("/fruits_name/{name}")
# async def get_fruits_name(
#     name: str = Path(..., description="this si fruits names", max_length=10),
#     quantity: int = Query(10, ge=1),
# ):
#     return JSONResponse({"fruit": name, "quantity": quantity})


# class FakeData(BaseModel):
#     first: str
#     second: int | None = None
#     third: bool
#     fourth: str | None = None


# @route.post("/fake")
# async def fake(data: FakeData):
#     return data


# @route.get("/example/{data}")
# async def example(data: Annotated[str, Path(..., description="the great one")]):
#     return JSONResponse({"message": data})


# @route.get("/example2")
# async def example2(data: Annotated[str, Query(..., description="the great second")]):
#     return data


# class ExampleThreeData(BaseModel):
#     item: str | None = None


# @route.post("/example3")
# async def example3(
#     item: Annotated[ExampleThreeData | None, Body(description="its the data")] = None
# ):
#     return item


# """there is another way you can provide meta data to the to the fiels as well as 'the params"""


# class Item(BaseModel):
#     name: Annotated[
#         str,
#         Field(
#             ...,
#             max_length=100,
#             min_length=5,
#             description="this is for the name of item.",
#         ),
#     ]
#     price: Annotated[
#         int,
#         Field(..., ge=1, le=100, description="this is for the description of an item."),
#     ]

#     model_config = {
#         "json_schema_extra": {"examples": [{"name": "anurag", "price": 10}]}
#     }


# @route.post("/items")
# async def create_item(item: Item):
#     return JSONResponse({"item name": item.name, "item price": item.price})


# # making instances of pydantic model and setting retun type of response in route
# @route.post("/itemsList")
# async def create_item_list(item: Item) -> list[Item]:
#     return [Item(name="anurag", price=20), Item(name="anuragggggggggggggggg", price=40)]


# # Form and File type annotation and data types from fastapi
# @route.post("/itemsList")
# async def create_item_list(
#     name: Annotated[str, Form()],
#     age: Annotated[int, Form()],
#     cv: UploadFile,
# ):
#     return "got it"


# # example of nested or sub dependency injection
# def query_extractor(q: str | None = None):
#     return q


# def query_or_cookie_extractor(
#     q: Annotated[str, Depends(query_extractor)],
#     last_query: Annotated[str | None, Cookie()] = None,
# ):
#     if not q:
#         return last_query
#     return q


# @route.get("/items/")
# async def read_query(
#     query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
# ):
#     return {"q_or_cookie": query_or_default}


# ----------------------------------------------------------------------------------------


# from motor.motor_asyncio import AsyncIOMotorClient
# from my_app.models.models import Item, ItemImage, ItemTag
# from beanie import init_beanie


# async def get_database() -> Generator:  # type: ignore
#     client = AsyncIOMotorClient("mongodb://localhost:27017")
#     await init_beanie(database=client.local, document_models=[Item, ItemImage, ItemTag])
#     yield
#     # await client.close()


# @route.post("/items/", response_model=Item_)
# async def create_item(item: Item_, db=Depends(get_database)):
#     item_doc = Item_(**item.model_dump())
#     print(item_doc)
#     await item_doc.create()
#     return item_doc


# # -------------------------------------------------------------------

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


# def verify_password(plain_password: str, hashed_password: str):
#     return pwd_context.verify(plain_password, hashed_password)


# # from fastapi import FastAPI, HTTPException, status, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select

# # from models import User, Base
# # from database import AsyncSessionLocal, engine
# from pydantic import BaseModel, EmailStr

# # from security import hash_password  # Assuming you have a hash_password utility function
# import asyncio


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# class UserCreate(BaseModel):
#     username: str
#     email: EmailStr
#     password: str


# from sqlalchemy.orm import Session


# @route.post("/signup/")
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     hashed_password = hash_password(user.password)
#     user = User(
#         username=user.username, email=user.email, hashed_password=hashed_password
#     )
#     db.add(user)
#     await db.commit()
#     await db.refresh(user)
#     return {"username": user.username, "email": user.email}
#     # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Signup failed")


# import jwt


# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=60)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, "my-secret", algorithm="HS256")
#     return encoded_jwt


# async def authenticate_user(username: str, password: str, db: AsyncSession):
#     async with db.begin():
#         query = select(User).filter(User.username == username)
#         result = await db.execute(query)
#         user = result.scalars().first()
#         if not user:
#             return False
#         if not verify_password(password, user.hashed_password):
#             return False
#         return {
#             "id": user.id,
#             "username": user.username,
#             "email": user.email,
#         }


# @route.post("/login_user")
# async def login_for_access_token(
#     user_data: UserCreate,
#     db: Session = Depends(get_db),
# ):
#     print(user_data)
#     user = await authenticate_user(user_data.username, user_data.password, db)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     print(">>>>>>>>>>>>>>>>>")
#     # access_token = create_access_token(data={"sub": user.username})
#     print("??????", user, type(user))
#     to_encode = user
#     expire = datetime.utcnow() + timedelta(minutes=60)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, "my-secret", algorithm="HS256")
#     print("+++++++++++++++++++++++++")
#     return {"access_token": encoded_jwt, "token_type": "bearer"}


# security_scheme = HTTPBearer()


# def verify_token(token: str):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     payload = jwt.decode(token, "my-secret", algorithms=["HS256"])
#     username: str = payload.get("username")
#     if username is None:
#         raise credentials_exception
#     # Here you can add more checks, e.g., is this username in the database?
#     return payload  # Or return a user object


# async def get_current_user(
#     credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
# ):
#     return verify_token(credentials.credentials)


# @route.get("/protected-endpoint")
# async def protected_endpoint(current_user=Depends(get_current_user)):
#     # If the token is invalid, an error would have been raised before reaching this point
#     return {
#         "message": "You have access to the protected endpoint",
#         "user": current_user,
#     }


# # this is how we can make a queryparams out of a dependecny function and return pydantic model instance to be used inside the route
# class UserQueryParams(BaseModel):
#     age: Optional[int] = Field(None, description="Filter users by age")
#     name: Optional[str] = Field(None, description="Filter users by name")


# def query_params(
#     age: Optional[int] = None, name: Optional[str] = None
# ) -> UserQueryParams:
#     return UserQueryParams(age=age, name=name)


# @route.get("/test/x")
# async def qparm_test(qp: UserQueryParams = Depends(query_params)):
#     return JSONResponse({"messgae": qp})


# # example below how you cna set up authentication flow with  Oauth2 password flow with bearer information(user inut)
# auth_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
#     )


# async def get_current_user(token: Annotated[str, Depends(auth_scheme)]):
#     user = fake_decode_token(token)
#     return user


# @route.post("/auth_token")
# async def get_token(current_user: Annotated[User, Depends(get_current_user)]):
#     return current_user


# --------------------------------------------------------------------------------------------------
# creating a flow for crud wih user auth with mongo db


# below here is how we can add User collection and add user to it ..
@route.post("/register_user_mongo")
async def register(user: UserMongo, db=Depends(db_connection)):
    user_data = dict(user)
    user_data["password"] = hash_password(user_data["password"])
    user = UserMongo(**user_data)
    await user.create()
    return ""


# now we will setup the authentication flow

from jose import jwt, JWTError


async def create_access_token(data: dict, db: Generator = Depends(db_connection)):

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "my-secret", "HS256")
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/t")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:

        payload = jwt.decode(token, "my-secret", "HS256")
        username_from_token = payload.get("sub")

        return username_from_token
    except JWTError:
        raise credentials_exception


@route.post("/t")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db=Depends(db_connection),
):
    user = {"username": form_data.username, "password": form_data.password}
    user_check = await UserMongo.find_one(UserMongo.username == form_data.username)

    if not user_check:
        print("here")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        access_token = await create_access_token(
            data={"username": user["username"], "password": user["password"]}
        )
        return {"access_token": access_token, "token_type": "bearer"}


@route.get("/check")
async def check(user: Annotated[any, Depends(get_current_user)]):
    print("user")
    return "got it"


# below will be the flow of postgres flow of authentication ..
