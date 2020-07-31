example = {
    {
        "type": "section",
        "text": {
            "text": "A message *with some bold text* and _some italicized text_.",
            "type": "mrkdwn",
        },
        "fields": [],
    }
}

field_headers = [
    {"type": "mrkdwn", "text": "*Nation*       *Turn*"},
]


def create_player_blocks(players):
    player_blocks = []

    for player in players.get("player_status"):
        nation_name = player.get("nation_name")
        turn_status = player.get("nation_turn_status")

        nation_dict = {"type": "plain_text", "text": f"{nation_name}       {turn_status}"}

        player_blocks.append(nation_dict)
    return player_blocks
