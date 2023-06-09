import uuid

import storage.models
from storage.db_manager import session

import app.dto


def create_event(event: app.dto.Event) -> uuid.UUID:
    with session() as db:
        value_id = uuid.uuid4()
        value = storage.models.Event(
            **(event.dict()),
            id=str(value_id)
        )
        db.add(value)
        db.commit()
    return value_id


def read_events(id: str | None = None) -> list[app.dto.EventResponse] | app.dto.EventResponse | None:
    result = None
    with session() as db:
        if id is None:
            result = db.query(storage.models.Event).all()
            return [app.dto.EventResponse.from_orm(value) for value in result]     
        result = db.get(storage.models.Event, id)
        return app.dto.EventResponse.from_orm(result) if result else result


def update_event(id: str, event: app.dto.Event) -> bool:
    with session() as db:
        if value := db.get(storage.models.Event, id):
            value.name = event.name # type: ignore
            value.date = event.date # type: ignore
            value.description = event.description # type: ignore
            db.commit()
            return True
        return False


def delete_event(id: str) -> bool:
    with session() as db:
        if value := db.get(storage.models.Event, id):
            db.delete(value)
            db.commit()
            return True
        return False
