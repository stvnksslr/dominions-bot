from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from pendulum import now
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Players(Base):
    __tablename__ = 'players'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    player_name = Column(String(250))
    game_id = Column(Integer, ForeignKey('game.id'))
    nation_id = Column(Integer)

    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now())
