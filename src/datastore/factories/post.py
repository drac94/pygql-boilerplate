from factory import LazyAttribute
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import Session
from datetime import datetime
from uuid import uuid4

from src.datastore.models import Post
from src.datastore.factories.providers import sfaker


class PostFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session: Session = None
        sqlalchemy_session_persistence = "flush"

    id = LazyAttribute(lambda _: uuid4())
    title = LazyAttribute(lambda _: sfaker.post_provider())
    content = LazyAttribute(lambda _: sfaker.post_provider())

    created_at = LazyAttribute(lambda _: datetime.utcnow())
    updated_at = LazyAttribute(lambda _: datetime.utcnow())
