import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
from sqlalchemy.util.compat import contextmanager

load_dotenv()


def create_session():
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


manual_session = create_session()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
