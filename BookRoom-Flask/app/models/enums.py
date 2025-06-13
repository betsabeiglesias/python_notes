from enum import Enum

class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"


class SpaceType(str, Enum):
    study = "study"
    lecture = "lecture"
    meeting = "meeting"


class ReservationStatus(str, Enum):
    active = "active"
    in_use = "in_use"
    completed = "completed"
    cancelled = "cancelled"