from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import respond_to

from json import dumps

from dominions.game_server_info import get_game_details


def create_player_blocks(players):
    player_blocks = []

    for player in players.get("player_status"):
        nation_name = player.get("nation_name")
        turn_status = player.get("nation_turn_status")

        nation_dict = {"type": "plain_text", "text": f"{nation_name}"}

        turn_dict = {"type": "plain_text", "text": f"{turn_status}"}

        player_blocks.append(nation_dict)
        player_blocks.append(turn_dict)
    return player_blocks


class TurnStatus(MachineBasePlugin):
    @respond_to(r"check (?P<game>\d+)")
    def info(self, msg, game):
        # https://snek.earth/api/games/1626
        game_details = get_game_details(game)
        print(f"game_details: {game_details}")
        game_name = game_details.get("game_status").name
        turn = game_details.get("game_status").turn

        field_headers = [
            {"type": "mrkdwn", "text": "*Nation*"},
            {"type": "mrkdwn", "text": "*Turn*"},
        ]

        raw_player_blocks = create_player_blocks(game_details)

        print("HELLO I MADE IT THIS FAR!")

        formatted_player_blocks = field_headers + raw_player_blocks

        formatted_msg = [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": "Dominions Times"},
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": " :freak_lord: *Update* :freak_lord:",
                },
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Game: {game_name} Turn: {turn}"},
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {"text": "*Player List*", "type": "mrkdwn"},
                "fields": formatted_player_blocks[:10],
            },
            {
                "type": "section",
                "text": {"text": ".", "type": "mrkdwn"},
                "fields": formatted_player_blocks[10:],
            },
        ]

        print("Formatted Slack Message: ")
        print(formatted_msg)

        msg.reply(text="", blocks=formatted_msg)
