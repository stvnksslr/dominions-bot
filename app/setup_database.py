import os

from pendulum import now
from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from pathlib import Path

from sqlalchemy.orm import sessionmaker

Base = declarative_base()

db_name = 'local.db'
path = Path.cwd().joinpath(db_name)
db_url = 'sqlite:///' + str(path)


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(250), nullable=True)
    alias = Column(String(250), nullable=True)
    turn = Column(Integer(), nullable=True)
    active = Column(Boolean(), default=True)

    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now())


class Players(Base):
    __tablename__ = 'players'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    player_name = Column(String(250))
    game_id = Column(Integer, ForeignKey('game.id'))

    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now())


if path.is_file():
    os.remove(db_name)
engine = create_engine(db_url)

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
