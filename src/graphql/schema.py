import graphene

from .queries import PostQuery

from .mutations import CreatePost, DeletePost, UpdatePost


class Query(PostQuery):
    pass


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    delete_post = DeletePost.Field()
    update_post = UpdatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
