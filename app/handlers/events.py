import uuid

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

import app.dto

import storage.events


event_router = APIRouter(prefix='/events', tags=['events'])


@event_router.get('/')
def get_all_events(start: int = 0, offset: int = 10) -> list[app.dto.EventResponse]:
    """
    Returns the **offset** of the events, starting from the event with the number **start** 
    """

    events = storage.events.read_events()
    return events[start : start + offset]


@event_router.get('/{id}')
def get_event(id: str) -> app.dto.EventResponse:
    """
    Returns single evrnt by it's ID
    """

    if event := storage.events.read_events(id):
        return event
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='Event not found')


@event_router.post('/')
def create_event(event: app.dto.Event) -> uuid.UUID:
    """
    Create new event
    """
    return storage.events.create_event(event)


@event_router.put('/{id}')
def update_event(id: str, event: app.dto.Event):
    """
    Change an existing event
    """
    result = storage.events.update_event(id, event)

    if result:
        return JSONResponse(status_code=status.HTTP_200_OK, content='Event updated')
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='Wrong id')


@event_router.delete('/{id}')
def delete_event(id: str):
    """
    Delete an existing event
    """

    result = storage.events.delete_event(id)

    if result:
        return JSONResponse(status_code=status.HTTP_200_OK, content='Event deleted')
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='Wrong id')
