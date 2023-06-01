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


def read_events(id: str | None = None) -> list[storage.models.Event] | storage.models.Event | None:
    result = None

    with session() as db:
        if id is None:
            result = db.query(storage.models.Event).all()
        else:
            result = db.get(storage.models.Event, id)
    
    return result


def update_event(id: str, event: app.dto.Event) -> bool:
    with session() as db:
        if value := db.get(storage.models.Event, id):
            value.name = event.name
            value.date = event.date
            value.description = event.description

            db.commit()

            return True
        else:
            return False



    

    