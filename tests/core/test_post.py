from sqlalchemy.orm import Session

from src.core import PostService
from src.datastore.factories import PostFactory

BATCH_CREATE = 10


def test_get_post_by_id(pg_session: Session, with_factories: None) -> None:
    post = PostFactory()
    result = PostService(pg_session).get(post.id)

    assert result
    assert post.id == result.id
    assert post.title == result.title
    assert post.content == result.content


def test_get_post_list(pg_session: Session, with_factories: None) -> None:

    PostFactory.create_batch(BATCH_CREATE)
    posts = PostService(pg_session).get_list()

    assert len(posts) == BATCH_CREATE
