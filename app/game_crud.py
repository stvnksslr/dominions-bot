from attr import dataclass

from app.game_server_info import get_game_details


@dataclass
class Game(object):
    server_id: int
    name: str
    turn: int
    players: list


def fetch_game(server_address):
    game_id = server_address.replace('snek.earth:', '')

    game_detail = get_game_details(game_id)
    game_status = game_detail.get('game_status')
    player_status = game_detail.get('player_status')

    new_game = Game(
        server_id=game_id,
        name=game_status.name,
        turn=game_status.turn,
        players=player_status)

    return new_game
