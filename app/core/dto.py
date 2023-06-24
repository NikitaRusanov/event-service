import dataclasses
from datetime import datetime

import app.core.logic


@dataclasses.dataclass
class Event:
    id: str
    event_name: str
    event_type: app.core.logic.EventType
    event_date: datetime | None = None
