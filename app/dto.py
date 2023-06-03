from __future__ import annotations

from typing import Any, Type
from pydantic import BaseModel, EmailStr
from datetime import date

import storage.models


class Event(BaseModel):
    name: str
    date: date
    description: str | None


class EventResponse(Event):
    id: str


    @classmethod
    def from_orm(cls, obj: storage.models.Event) -> EventResponse:
        return cls(
            name = str(obj.name),
            date = obj.date, # type: ignore
            description = obj.description, # type: ignore
            id = obj.id # type: ignore
        )


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    following_events: list[str]
    