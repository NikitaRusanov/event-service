from pydantic import BaseModel
from datetime import date


class Event(BaseModel):
    name: str
    date: date
    description: str | None
