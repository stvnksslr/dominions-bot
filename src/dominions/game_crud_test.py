from dominions.game_server_info import get_game_details
from dominions.game_crud import fetch_game

server_info = "snek.earth:33533"
server_id = 30604


def test__fetch_game():
    game_info = fetch_game(server_info)
    assert bool(game_info) is True


def test__fetch_game_details():
    game_details = get_game_details("33533")
    assert bool(game_details) is True
