from contextlib import contextmanager
from typing import Generator, List

from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import Session

from .post import PostFactory


@contextmanager
def active_factories(
    session: Session, factories: List[SQLAlchemyModelFactory]
) -> Generator[None, None, None]:
    for f in factories:
        f._meta.sqlalchemy_session = session
    yield
    for f in factories:
        f._meta.sqlalchemy_session = None


all_factories = [PostFactory]

__all__ = ("active_factories", "PostFactory", "all_factories")
