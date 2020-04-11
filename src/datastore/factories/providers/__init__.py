from faker import Faker

from src.datastore.factories.providers.post_provider import PostProvider

sfaker = Faker()
sfaker.add_provider(PostProvider)

__all__ = ("sfaker",)
