from typing import Generator

from pytest import fixture
from sqlalchemy.orm import Session

from src.datastore.factories import active_factories, all_factories
from src.datastore.models import BaseModel
from src.datastore.db_store import get_session


@fixture(scope="session")
def pg_scoped_session() -> Generator[Session, None, None]:
    """Create a SQLAlchemy session, tied to the pytest session scope
    This fixture instantiates a SQLAlchemy session and prepares the database before
    running tests. It then drops all database tables when tests are done.
    """
    session_class = get_session()
    session = session_class()
    bind = session.get_bind()
    BaseModel.metadata.drop_all(bind)
    BaseModel.metadata.create_all(bind)

    try:
        yield session
    finally:
        BaseModel.metadata.drop_all(bind)
        session_class.remove()


@fixture
def pg_session(pg_scoped_session: Session) -> Generator[Session, None, None]:
    """Initiate a transaction before each test function"""

    pg_scoped_session.begin()

    try:
        yield pg_scoped_session
    finally:
        pg_scoped_session.rollback()


@fixture
def with_factories(pg_session: Session.__class__) -> Generator[None, None, None]:
    with active_factories(pg_session, all_factories):
        yield None
