import pathlib
import json

from dataclasses import dataclass
from enum import Enum

BASE_PATH = pathlib.Path.cwd() / "src" / "dominions" / "tests"

mock_game_status_path = BASE_PATH / "mocks" / "snek_status.json"
mock_game_details_path = BASE_PATH / "mocks" / "snek_details.json"


class Era(Enum):
    Early_Age = 0
    Middle_Age = 1
    Late_Age = 2


class PlayerType(Enum):
    Empty = 0
    Human = 1
    Bot = 2
    Independent = 3
    Closed = 253
    Defeated_this_turn = 254
    Defeated = 255
    eliminated_player = -1
    Defeated_Duplicate = -2


class TurnStatus(Enum):
    NotSubmitted = 0
    PartiallySubmitted = 1
    Submitted = 2


@dataclass
class Nation:
    id: int
    name: str
    epithet: str


@dataclass
class Player:
    nation: Nation
    player_type: PlayerType


@dataclass
class Thrones:
    lvl_1_thrones: int
    lvl_2_thrones: int
    lvl_3_thrones: int


@dataclass
class ServerStatus:
    id: str
    name: str
    turn: str
    port: str
    turn_duration: str


MOCK_SERVER_STATUS = ServerStatus(1770, "The Earliest Boi", "null", "31770", 48)


def update_server_status(server_status) -> ServerStatus:
    game_id = server_status.get("id")
    name = server_status.get("name")
    turn = "null"
    port = f"3{game_id}"
    turn_duration = server_status.get("hours")

    new_server_status = ServerStatus(game_id, name, turn, port, turn_duration)

    return new_server_status


def test__process_game_details():
    with open(mock_game_details_path, "r") as file:
        data = json.load(file)
        new_server_status = update_server_status(server_status=data)

        assert new_server_status == MOCK_SERVER_STATUS