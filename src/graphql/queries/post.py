from typing import List

import graphene
from graphql import ResolveInfo
from uuid import UUID

from src.core import PostService
from src.graphql.types import PostType
from src.datastore.models import Post


class PostQuery(graphene.ObjectType):
    posts = graphene.List(graphene.NonNull(PostType), required=True)
    post = graphene.Field(PostType, id=graphene.ID())

    def resolve_posts(self, info: ResolveInfo) -> List[PostType]:
        return PostService(info.context.get("session")).get_list()

    def resolve_post(self, info: ResolveInfo, id: UUID) -> Post:
        return PostService(info.context.get("session")).get(id)
