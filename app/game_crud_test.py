from unittest import TestCase

from app.game_crud import add_game
from old_app.game_server_info import get_game_details


class GameCrudTest(TestCase):

    def setUp(self):
        self.mock_game_id = 604

    def test__create_new_game(self):
        game_detail = get_game_details(self.mock_game_id)
        game_status = game_detail.get('game_status')
        player_status = game_detail.get('player_status')
        game_id = self.mock_game_id
        new_game = add_game(game_id, game_status, player_status)

        self.assertTrue(new_game)
