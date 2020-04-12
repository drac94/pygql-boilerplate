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


def test_create_post(pg_session: Session, with_factories: None) -> None:
    post = PostService(pg_session).create("title", "content")

    assert post


def test_update_post(pg_session: Session, with_factories: None) -> None:

    updated_title = "title updated"
    updated_contnet = "content updated"

    post = PostFactory()
    updated_post = PostService(pg_session).update(
        post.id, updated_title, updated_contnet
    )

    assert updated_post
    assert updated_post.id == post.id
    assert updated_post.title == updated_title
    assert updated_post.content == updated_contnet


def test_delete_post_by_id(pg_session: Session, with_factories: None) -> None:

    post = PostFactory()
    posts = PostService(pg_session).get_list()

    assert len(posts) == 1

    PostService(pg_session).delete(post.id)

    posts = PostService(pg_session).get_list()

    assert len(posts) == 0
