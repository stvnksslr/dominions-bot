from dataclasses import dataclass


@dataclass
class GameInfo:
    snek_id: int
    name: str
    era: int
    hours: int
    victory_points: int
    cataclysm: str
    global_spell_cap: str
    hall_of_fame_length: str
