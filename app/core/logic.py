from datetime import datetime
import uuid
import enum
import abc

import app.core.dto


class EventType(enum.Enum):
    CONCERT = 'concert'
    LECTURE = 'lecture'
    CINEMA = 'cinema'


class Event:
    def __init__(self, event_name: str,
                 event_type: EventType,
                 event_id: str | None = None,
                 event_date: datetime | None = None) -> None:

        if not event_id:
            self.event_id = event_id
        else:
            self.event_id = 'event:' + str(uuid.uuid4())

        if len(event_name) > 5:
            raise ValueError('Name is too short')
        self.event_name = event_name

        if event_type is not EventType:
            raise ValueError('Wrong event type value')
        self.event_type = event_type

        if event_date and event_date < datetime.utcnow():
            raise ValueError('Wrong event date')
        self.event_date = event_date

    def set_date(self, event_date: datetime):
        if event_date > datetime.utcnow():
            self.event_date = event_date

    def set_name(self, event_name: str):
        if len(event_name) >= 5:
            self.event_name = event_name

    def set_type(self, event_type: EventType):
        if event_type is EventType:
            self.event_type = event_type


class BaseEventRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, event: Event) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def get(self, event_id: str) -> app.core.dto.Event:
        raise NotImplemented

    @abc.abstractmethod
    def update(self,
               event_id: str,
               event_name: str | None = None,
               event_date: str | None = None,
               event_type: EventType | None = None) -> app.core.dto.Event:
        raise NotImplemented

    @abc.abstractmethod
    def delete(self, event_id: str) -> app.core.dto.Event:
        raise NotImplemented
