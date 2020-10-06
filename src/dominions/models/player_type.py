from enum import Enum


class PlayerType(Enum):
    Empty = 0
    Human = 1
    Computer = 2
    Independent = 3
    Closed = 253
    Defeated_this_turn = 254
    Defeated = 255
