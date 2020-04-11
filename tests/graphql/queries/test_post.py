from sqlalchemy.orm import Session

from src.graphql import schema
from src.datastore.factories import PostFactory


def test_list_posts_should_be_successful(
    with_factories: None, pg_session: Session
) -> None:
    PostFactory.create_batch(5)

    query = "{allPosts {id title}}"
    context = {"session": pg_session}
    result = schema.execute(query, context=context)

    assert not result.errors
    assert len(result.data["allPosts"]) == 5
