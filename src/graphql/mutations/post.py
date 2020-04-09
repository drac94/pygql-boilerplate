from typing import Any, Dict

import graphene
from graphql import ResolveInfo

from src.graphql.types import PostType
from src.core import PostService


class PostInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    content = graphene.String(required=True)


class CreatePost(graphene.Mutation):
    class Arguments:
        post_data = PostInput(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info: ResolveInfo, post_data: Dict[str, Any]) -> Any:

        new_post = PostService(info.context.get("session")).create(
            title=post_data["title"], content=post_data["content"]
        )

        return CreatePost(new_post)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info: ResolveInfo, id: str, title: str, content: str) -> Any:

        updated_post = PostService(info.context.get("session")).update(
            id=id, title=title, content=content
        )

        return UpdatePost(updated_post)


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info: ResolveInfo, id: str) -> Any:

        deleted_post = PostService(info.context.get("session")).delete(id=id)

        return DeletePost(deleted_post)
