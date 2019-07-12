from discord import Embed

from app.server import get_game_status, get_player_status


async def get_game_details(game_id):
    game_status = get_game_status(game_id)
    player_status = get_player_status(game_id)

    block, response = await format_game_details(game_status, player_status)
    return block, response


async def format_game_details(game_status, player_status):
    game_name = game_status.name
    turn = "Turn: {}".format(game_status.turn)
    newline = " \n"
    response = Embed(title=game_name, description=turn, color=0x00FF00)
    block = ""
    for player in player_status.items():
        player_name = player[0]
        nation_id = player[1].get("nation_id")
        player_type = player[1].get("nation_controller")
        turn_status = player[1].get("nation_turn_status")

        if turn_status == "Submitted":
            turn_status = "✓"
        else:
            turn_status = "X"

        block = block + "{} {}({}): {} {}".format(
            turn_status, player_name, nation_id, player_type, newline
        )
    return block, response
