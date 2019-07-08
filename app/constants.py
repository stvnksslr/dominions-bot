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
class GameStatus:
    name: str
    era: str
    turn: str


@dataclass
class Nation:
    id: int
    name: str
    era: Era


PACKET_HEADER = "<ccLB"
PACKET_BYTES_PER_NATION = 3
PACKET_NUM_NATIONS = 250
PACKET_GENERAL_INFO = "<BBBBBB{0}sBBBBBBLB{1}BLLB"  # to use format later
PACKET_NATION_INFO_START = 15

mock_address = "snek.earth"
mock_address_ip = "172.19.134.2"
mock_port = 30604
