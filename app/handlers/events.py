from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

import uuid

import app.dto

import storage.events


event_router = APIRouter(prefix='/events', tags=['events'])


@event_router.get('/')
def get_all_events(start: int = 0, offset: int = 10) -> list[app.dto.EventResponse]:
    """
    Returns the **offset** of the events, starting from the event with the number **start** 
    """

    db_respones = storage.events.read_events()

    if db_respones is not None:
        events = [app.dto.EventResponse.from_orm(value) for value in db_respones] # type: ignore

    return events[start : start + offset]


@event_router.get('/{id}')
def get_event(id: str) -> app.dto.EventResponse:
    """
    Returns single evrnt by it's ID
    """
    db_response = storage.events.read_events(id)
    
    if db_response is not None:
        event = app.dto.EventResponse.from_orm(db_response) # type: ignore
        return event

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content='Wrong ID') # type: ignore


@event_router.post('/')
def create_event(event: app.dto.Event) -> uuid.UUID:
    """
    Create new event
    """
    return storage.events.create_event(event)


@event_router.put('/{id}') 
def update_event(id: int, event: app.dto.Event) -> app.dto.Event:
    """
    Change an existing event
    """
    return {'id': id, 'event': event}


@event_router.delete('/{id}')
def delete_event(id: int) -> app.dto.Event:
    """
    Delete an existing event
    """
    return {'id': id}
