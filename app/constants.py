from dataclasses import dataclass
from enum import Enum


class Era(Enum):
    Early_Age = 1
    Middle_Age = 2
    Late_Age = 3


class NationType(Enum):
    Empty = 0
    Human = 1
    AI = 2
    Independent = 3
    Closed = 253
    Defeated_this_turn = 254
    Defeated = 255


class TurnStatus(Enum):
    NotSubmitted = 0
    PartiallySubmitted = 1
    Submitted = 2


@dataclass
class Nation:
    id: int
    name: str
    era: Era
