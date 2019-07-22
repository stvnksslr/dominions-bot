from pendulum import now
from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, DateTime, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, Sequence('game_id_seq'), primary_key=True)
    server_id = Column(Integer(), nullable=True)
    name = Column(String(250), nullable=True)
    alias = Column(String(250), nullable=True)
    turn = Column(Integer(), nullable=True)
    active = Column(Boolean(), default=True)
    players = Column(JSON, nullable=True)

    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now())


class Players(Base):
    __tablename__ = 'players'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    player_name = Column(String(250))
    game_id = Column(Integer, ForeignKey('game.id'))

    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now())
