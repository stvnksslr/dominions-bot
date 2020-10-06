from httpx import get, HTTPStatusError

from dominions.constants import SNEK_BASE_URL
from dominions.models.turn_status import TurnStatus
from dominions.models.player_type import PlayerType
from dominions.models.player import Player
from dominions.models.game_info import GameInfo


def fetch_game_info(game_id):
    try:
        game_info = get(f"{SNEK_BASE_URL}{game_id}")
        return game_info
    except HTTPStatusError as error_message:
        raise error_message


def fetch_player_status(game_id):
    try:
        player_status = get(f"{SNEK_BASE_URL}{game_id}/status")
        return player_status
    except HTTPStatusError as error_message:
        raise error_message


def process_player_status(player_status):
    formatted_player_list = []
    nations = player_status.get("nations")

    for player in nations:
        formatted_player = Player(
            nation_id=player.get("nationid"),
            nation_name=player.get("name"),
            player_type=PlayerType(int(player.get("controller"))).name,
            turn_status=TurnStatus(int(player.get("turnplayed"))).name,
        )
        formatted_player_list.append(formatted_player)
    return formatted_player_list


def process_game_info(game_info):
    GameInfo(
        snek_id=game_info.get("id"),
        name=game_info.get("name"),
        port=f"3{game_info.get('id')}",
        era=game_info.get("era"),
        hours=game_info.get("hours"),
        victory_points=game_info.get("requiredap"),
        cataclysm=game_info.get("cataclysm") or None,
        global_spell_cap=game_info.get("globals"),
        hall_of_fame_length=game_info.get("hofsize"),
    )
    return GameInfo
