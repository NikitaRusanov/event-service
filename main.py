from fastapi import FastAPI

from app.handlers.events import event_router


app = FastAPI(title='Events service')


app.include_router(event_router)