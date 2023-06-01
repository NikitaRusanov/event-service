from fastapi import APIRouter
import uuid

import app.dto

import storage.events


event_router = APIRouter(prefix='/events', tags=['events'])


@event_router.get('/')
def get_all_events(start: int = 0, offset: int = 10) -> list[app.dto.Event]:
    """
    Returns the **offset** of the events, starting from the event with the number **start** 
    """
    return {'start': start, 'offset': offset}


@event_router.get('/{id}')
def get_event(id: int) -> app.dto.Event:
    """
    Returns single evrnt by it's ID
    """
    return {'id': id}


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
