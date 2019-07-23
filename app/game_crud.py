from discord import Embed

from app.config import manual_session
from app.game_server_info import get_game_details
from app.models import Game


def add_game(server_address):
    game_id = server_address.replace('snek.earth:', '')
    existing_game = manual_session.query(Game).filter_by(server_id=game_id).first()

    if existing_game:
        return existing_game
    else:
        game_detail = get_game_details(game_id)
        game_status = game_detail.get('game_status')
        player_status = game_detail.get('player_status')

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
        game = manual_session.query(Game).filter_by(id=game_id).first()
        game.turn = game_status[0].get('turn')
        game.players = player_status
        manual_session.add(game)
        manual_session.commit()
        return game
    except Exception as e:
        print('error could not update!')


def delete_game(game_id, alias):
    if game_id:
        game = manual_session.query(Game).filter_by(id=game_id)
        manual_session.delete(game)
    if alias:
        game = manual_session.query(Game).filter_by(alias=alias)
        manual_session.delete(game)
    return


def fetch_game(server_address):
    game = manual_session.query(Game).filter_by(server_id=server_address).first()
    return game
