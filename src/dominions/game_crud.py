from dominions.models.game import Game
import json
import requests
from dominions.models.turn_status import TurnStatus
from dominions.models.nation_type import NationType
from dominions.models.game_status import GameStatus
from dominions.server_status import query


def get_game_status(game_id):
    game_status = json.loads(
        requests.get(f"https://dom5.snek.earth/api/games/{game_id}").content
    )
    game_name = game_status["name"]

    raw_game_info = query(address="snek.earth", port=int(f"3{game_id}"))

    return GameStatus(
        name=game_name,
        hours=raw_game_info.hours,
        required_ap=raw_game_info.required_ap,
        cataclysm=raw_game_info.cataclysm,
    )


def get_player_status(game_id):
    player_status = json.loads(
        requests.get(f"https://dom5.snek.earth/api/games/{game_id}/status").content
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


def get_game_details(port):
    game_id = port[1:]
    game_status = get_game_status(game_id)
    player_status = get_player_status(game_id)

    return {"game_status": game_status, "player_status": player_status}


def fetch_game(server_address):
    game_id = server_address.replace("snek.earth:", "")

    game_detail = get_game_details(game_id)
    game_status = game_detail.get("game_status")
    player_status = game_detail.get("player_status")

    new_game = Game(
        server_id=game_id,
        name=game_status.name,
        turn=game_status.turn,
        players=player_status,
    )

    return new_game
