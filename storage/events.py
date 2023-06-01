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

    