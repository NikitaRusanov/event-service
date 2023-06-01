from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, DateTime, Text


class Base(DeclarativeBase): pass


class Event(Base):
    __tablename__ = 'events'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(Text)
