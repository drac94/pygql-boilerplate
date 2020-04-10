from typing import List

import graphene
from graphql import ResolveInfo

from src.core import PostService
from src.graphql.types import PostType


class PostQuery(graphene.ObjectType):
    post = graphene.List(graphene.NonNull(PostType), required=True)

    def resolve_post(self, info: ResolveInfo) -> List[PostType]:
        return PostService(info.context.get("session")).get_list()
