import datetime
import uuid
import enum
import abc


class EventType(enum.Enum):
    CONCERT = 'concert'
    LECTURE = 'lecture'
    CINEMA = 'cinema'


class Event:
    def __init__(self, event_name: str, 
                 event_type: EventType, 
                 event_date: datetime.datetime | None = None) -> None:

        self.event_id = uuid.uuid4()
        self.event_name = event_name
        self.event_type = event_type
        
        if event_date and event_date < datetime.datetime.utcnow():
            raise ValueError('Wrong event date')
        self.event_date = event_date


