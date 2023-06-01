from fastapi import FastAPI

from app.handlers.events import event_router

from storage.models import Base
from storage.db_manager import engine


Base.metadata.create_all(engine)


app = FastAPI(title='Events service')


app.include_router(event_router)