from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import respond_to

from dominions.game_server_info import get_game_details


def create_player_blocks(players):
    player_blocks = []

    for player in players.get("player_status"):
        nation_name = player.get("nation_name")
        turn_status = player.get("nation_turn_status")

        turn_status_emoji = ""
        if turn_status == "NotSubmitted":
            turn_status_emoji = ":x:"
        else:
            turn_status_emoji = ":white_check_mark:"

        nation_section = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f" {turn_status_emoji} *{nation_name}*"},
        }

        player_blocks.append(nation_section)
    print("LOOK AT ME")
    print(player_blocks)
    return player_blocks


def pull_game_details(game):
    game_name, turn, raw_player_blocks = fetch_game_details(game)

    formatted_msg = [
        {"type": "header", "text": {"type": "plain_text", "text": "Dominions Times"},},
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": " :freak_lord: *Update* :freak_lord:",},
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"{game_name} Turn: {turn}"},
        },
        {"type": "divider"},
        {"type": "section", "text": {"type": "mrkdwn", "text": "*Player List*"}},
    ]
    test_list = formatted_msg + raw_player_blocks

    print(test_list)

    return test_list


def fetch_game_details(game):
    # https://snek.earth/api/games/1626
    game_details = get_game_details(game)
    game_name = game_details.get("game_status").name
    turn = game_details.get("game_status").turn
    raw_player_blocks = create_player_blocks(game_details)
    return game_name, turn, raw_player_blocks


class TurnStatus(MachineBasePlugin):
    @respond_to(r"check (?P<game>\d+)")
    def info(self, msg, game):
        formatted_msg = pull_game_details(game)
        msg.reply(text="", blocks=formatted_msg)
