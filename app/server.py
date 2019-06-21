import json
from dataclasses import dataclass

import requests

from app.constants import Era, TurnStatus, NationType

mock_game_id = 604


@dataclass
class GameStatus:
    game_name: str
    era: str
    next_turn: str


def get_game_status(game_id=mock_game_id):
    game_status = json.loads(requests.get('https://dom5.snek.earth/api/games/{}'.format(game_id)).content)
    game_name = game_status['name']
    era = Era(game_status['era']).name
    next_turn = game_status['hours']
    return GameStatus(game_name, era, next_turn)


game_status = get_game_status()
print('cats are cool')

def get_player_status():
    player_status = json.loads(requests.get('https://dom5.snek.earth/api/games/{}/status'.format(game_id)).content)
    player_count = len(player_status['nations'])
    player_nations = player_status['nations']
    for nation in player_nations:
        nation_id = nation['nationid']
        nation_name = nation['name']
        nation_epithet = nation['epithet']
        nation_controller = NationType(int(nation['controller'])).name
        nation_turn_status = TurnStatus(int(nation['turnplayed'])).name
