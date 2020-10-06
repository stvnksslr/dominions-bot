from dataclasses import dataclass
from dominions.models.player_type import PlayerType
from dominions.models.turn_status import TurnStatus


@dataclass
class Player:
    nation_id: str
    nation_name: str
    player_type: PlayerType
    turn_status: TurnStatus
