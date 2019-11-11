from unittest import TestCase

from app.game_crud import fetch_game


class GameCrudTest(TestCase):

    def setUp(self):
        self.server_info = "snek.earth:30604"
        self.server_id = 30604

    def test__fetch_game(self):
        game_info = fetch_game(self.server_info)
        self.assertTrue(game_info)
