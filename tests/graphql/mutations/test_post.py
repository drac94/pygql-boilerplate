from sqlalchemy.orm import Session
from uuid import uuid4

from src.graphql import schema
from src.datastore.factories import PostFactory


def get_create_mutation(title: str, content: str) -> str:
    return f"""
    mutation createPost {{
        createPost(postData:{{title:"{title}", content:"{content}"}}) {{
            post {{
                id
                title
                content
            }}
        }}
    }}"""


def get_update_mutation(id: str, title: str, content: str) -> str:
    return f"""
    mutation updatePost {{
        updatePost(id: "{id}", title:"{title}", content:"{content}") {{
            post {{
                id
                title
                content
            }}
        }}
    }}"""


def get_delete_mutation(id: str) -> str:
    return f"""
    mutation deletePost {{
        deletePost(id: "{id}") {{
            post {{
                id
                title
                content
            }}
        }}
    }}"""


def test_create_post_should_be_successful(
    with_factories: None, pg_session: Session
) -> None:
    PostFactory.create_batch(5)

    query = get_create_mutation("title", "content")
    context = {"session": pg_session}
    result = schema.execute(query, context=context)

    assert not result.errors
    assert result.data
    assert result.data["createPost"]["post"]


def test_update_post_should_be_successful(
    with_factories: None, pg_session: Session
) -> None:
    post = PostFactory()

    updated_title = "title updated"
    updated_contnet = "content updated"

    query = get_update_mutation(post.id, updated_title, updated_contnet)
    context = {"session": pg_session}
    result = schema.execute(query, context=context)

    assert not result.errors
    assert result.data
    assert result.data["updatePost"]["post"]
    assert result.data["updatePost"]["post"]["title"] == updated_title
    assert result.data["updatePost"]["post"]["content"] == updated_contnet


def test_update_post_with_wrong_id_should_not_be_successful(
    with_factories: None, pg_session: Session
) -> None:

    updated_title = "title updated"
    updated_contnet = "content updated"

    query = get_update_mutation(uuid4(), updated_title, updated_contnet)
    context = {"session": pg_session}
    result = schema.execute(query, context=context)

    assert result.errors


def test_delete_post_should_be_successful(
    with_factories: None, pg_session: Session
) -> None:
    post = PostFactory()

    post_id = str(post.id)

    query = get_delete_mutation(post_id)
    context = {"session": pg_session}
    result = schema.execute(query, context=context)

    assert not result.errors
    assert result.data
    assert result.data["deletePost"]["post"]
    assert result.data["deletePost"]["post"]["id"] == post_id


def test_delete_post_with_wrong_id_should_not_be_successful(
    with_factories: None, pg_session: Session
) -> None:

    query = get_delete_mutation(uuid4())
    context = {"session": pg_session}
    result = schema.execute(query, context=context)

    assert result.errors
