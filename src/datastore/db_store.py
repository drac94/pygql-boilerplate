from contextlib import contextmanager
from typing import Generator, Type

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.session import Session

session_class = None


def get_session() -> Type[Session]:
    global session_class

    if not session_class:
        engine = create_engine("postgresql+psycopg2://user@host/pygql")
        session_factory = sessionmaker(bind=engine, autocommit=True)
        session_class = scoped_session(session_factory)

    return session_class


@contextmanager
def session_context() -> Generator[Session, None, None]:
    session_class = get_session()
    session = session_class()

    yield session

    try:
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session_class.remove()
