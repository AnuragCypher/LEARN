from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError


async def create_access_token(user: dict):
    to_encode = user.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_token = jwt.encode(to_encode, "my-secret", "HS256")
    return encoded_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:

        payload = jwt.decode(token, "my-secret", "HS256")

        return payload
    except JWTError:
        raise credentials_exception
