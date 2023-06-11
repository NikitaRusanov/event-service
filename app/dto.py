from __future__ import annotations

from typing import Any, Type
from pydantic import BaseModel, EmailStr
from datetime import date
from enum import Enum

import storage.models


class Event(BaseModel):
    name: str
    date: date
    description: str | None


class EventResponse(Event):
    id: str
    followed_users: list[int] | None = None


    @classmethod
    def from_orm(cls, obj: storage.models.Event) -> EventResponse:
        return cls(
            name = obj.name,
            date = obj.date, # type: ignore
            description = obj.description, # type: ignore
            id = obj.id, # type: ignore
            followed_users = [user.id for user in obj.followed_users]
        )


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    following_events: set[str] | None = None


class UserResponse(User):
    id: int

    @classmethod
    def from_orm(cls, obj: storage.models.User) -> UserResponse:
        #print(obj.following_events)
        return cls(
            id = obj.id,
            name=obj.name,
            email=obj.email,
            password=obj.password,
            following_events=[event.id for event in obj.following_events]
        )
    

class ResultCode(Enum):
    OK = 0
    WRONG_PASS = 1
    NOT_FOUND = 2
    USER_NOT_FOUND = 3
    EVENT_NOT_FOUND = 4