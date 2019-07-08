import json
import requests
from app.constants import Era, TurnStatus, NationType, GameStatus

mock_game_id = 604


def get_game_status(game_id=mock_game_id):
    game_status = json.loads(
        requests.get("https://dom5.snek.earth/api/games/{}".format(game_id)).content
    )
    game_name = game_status["name"]
    era = Era(game_status["era"]).name
    next_turn = game_status["hours"]
    return GameStatus(name=game_name, turn=None)


def get_player_status(game_id=mock_game_id):
    player_status = json.loads(
        requests.get(
            "https://dom5.snek.earth/api/games/{}/status".format(game_id)
        ).content
    )

    player_list = {}

    player_count = len(player_status["nations"])
    player_nations = player_status["nations"]
    for nation in player_nations:
        nation_id = nation["nationid"]
        nation_name = nation["name"]
        nation_epithet = nation["epithet"]
        nation_controller = NationType(int(nation["controller"])).name
        nation_turn_status = TurnStatus(int(nation["turnplayed"])).name

        nation_info = {
            "nation_id": nation_id,
            "nation_epithet": nation_epithet,
            "nation_controller": nation_controller,
            "nation_turn_status": nation_turn_status,
        }

        player_list.update({nation_name: nation_info})
    return player_list


game_status = get_game_status()
player_status = get_player_status()

print("this is a break")
