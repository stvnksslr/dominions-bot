from dominions.server import get_game_status, get_player_status


def get_game_details(port):
    game_id = port[1:]
    game_status = get_game_status(game_id)
    player_status = get_player_status(game_id)

    return {"game_status": game_status, "player_status": player_status}
