from unittest import TestCase

from app.game_crud import add_game, fetch_game


class GameCrudTest(TestCase):

    def setUp(self):
        self.server_info = "snek.earth:30604"
        self.server_id = 30604

    def test__create_new_game(self):
        new_game = add_game(server_address=self.server_info)

        self.assertTrue(new_game)

    def test__fetch_game(self):
        game_info = fetch_game(self.server_id)
        self.assertTrue(game_info)
