from dominions.game_crud import get_game_details, get_game_status, fetch_game


def test__fetch_snake_rest():
    assert True


# TODO: these are old and bad and make real calls
def test__fetch_game():
    game_info = fetch_game("snek.earth:31626")
    assert bool(game_info) is True


def test__fetch_game_details():
    game_details = get_game_details("31626")
    assert bool(game_details) is True


def test__fetch_game_status():
    game_status = get_game_status("1626")
    assert True
    