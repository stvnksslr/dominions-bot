from unittest import TestCase

from dominions.game_server_info import get_game_details
from dominions.game_crud import fetch_game


class GameCrudTest(TestCase):
    def setUp(self):
        self.server_info = "snek.earth:31626"
        self.server_id = 30604

    def test__fetch_game(self):
        game_info = fetch_game(self.server_info)
        self.assertTrue(game_info)

    def test__fetch_game_details(self):
        game_details = get_game_details("31626")
        self.assertTrue(game_details)
