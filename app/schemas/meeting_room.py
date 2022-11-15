from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(min_length=1, max_length=100)

    @validator('name')
    def name_not_empty(cls, value: str) -> str:
        if not value:
            raise ValueError('Название переговорки не должно быть пустым!')
        return value


class MeetingRoomUpdate(MeetingRoomBase):
    @validator('name')
    def name_cannot_be_null(cls, value: str) -> str:
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomDB(MeetingRoomBase):
    id: int

    class Config:
        orm_mode = True
