from app.config import manual_session
from app.models import Game


def add_game(game_id, game_status, player_status):
    new_game = Game(
        server_id=game_id,
        name=game_status.name,
        turn=game_status.turn,
        players=player_status)

    manual_session.add(new_game)
    manual_session.commit()
    return new_game


def update_game(game_id, game_status, player_status):
    try:
        game = Game.query.filter_by(id=game_id).first()
        game.turn = game_status[0].get('turn')
        game.players = player_status
    except Exception as e:
        print('error could not update!')


def delete_game(self):
    pass
