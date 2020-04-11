from faker.providers import BaseProvider
from typing import Tuple


class PostProvider(BaseProvider):
    PROVIDERS = ("string1", "string2", "string3")

    def post_provider(self) -> Tuple[str, str]:
        return self.random_element(self.PROVIDERS)
