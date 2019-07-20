from app.game_server_info import get_game_details
from app.setup_database import Game

game_id = 604
game_details = get_game_details(game_id)

print('hello')

create_game = Game(name=game_details.get('game_status').name, turn=game_details.get('game_status').turn)

dbsession.add(newToner)
dbsession.flush()
