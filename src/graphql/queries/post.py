from typing import List

import graphene
from graphql import ResolveInfo

from src.core import PostService
from src.graphql.types import PostType


class PostQuery(graphene.ObjectType):
    all_posts = graphene.List(graphene.NonNull(PostType), required=True)

    def resolve_all_posts(self, info: ResolveInfo) -> List[PostType]:
        return PostService(info.context.get("session")).get_list()
