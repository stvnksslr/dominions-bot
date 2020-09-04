from dataclasses import dataclass


@dataclass
class GameStatus:
    name: str
    turn: str
    hours: int
    required_ap: int
    cataclysm: str
