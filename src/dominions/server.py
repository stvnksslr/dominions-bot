import json
import requests
from dominions.constants import TurnStatus, NationType, GameStatus
from dominions.server_status import query


def get_game_status(game_id):
    game_status = json.loads(
        requests.get("https://dom5.snek.earth/api/games/{}".format(game_id)).content
    )
    game_name = game_status["name"]

    raw_game_info = query(address="snek.earth", port=int(f"3{game_id}"))
    return GameStatus(
        name=game_name,
        turn=raw_game_info.turn,
        hours_remaining=raw_game_info.hours_remaining,
    )


def get_player_status(game_id):
    player_status = json.loads(
        requests.get(
            "https://dom5.snek.earth/api/games/{}/status".format(game_id)
        ).content
    )

    player_list = []
    player_nations = player_status["nations"]
    for nation in player_nations:
        nation_id = nation["nationid"]
        nation_name = nation["name"]
        nation_epithet = nation["epithet"]
        nation_controller = NationType(int(nation["controller"])).name
        nation_turn_status = TurnStatus(int(nation["turnplayed"])).name

        nation_info = {
            "nation_name": nation_name,
            "nation_id": nation_id,
            "nation_epithet": nation_epithet,
            "nation_controller": nation_controller,
            "nation_turn_status": nation_turn_status,
        }

        player_list.append(nation_info)
    return player_list
