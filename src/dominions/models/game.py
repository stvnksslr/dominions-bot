from dataclasses import dataclass


@dataclass
class Game:
    server_id: int
    name: str
    turn: int
    players: list
