from datetime import date
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    birthdate: Optional[date]


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    birthdate: Optional[date]


class UserUpdate(schemas.BaseUserUpdate):
    pass
