import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from src.datastore.models.post import Post


class PostType(SQLAlchemyObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    content = graphene.String(required=True)

    class Meta:
        model = Post
