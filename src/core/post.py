from typing import List, Optional
from uuid import uuid4

from sqlalchemy.orm.session import Session
from src.datastore.models import Post


class PostService(object):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, id: str) -> Optional[Post]:
        return self.session.query(Post).get(id)

    def get_list(self) -> List[Post]:

        query = self.session.query(Post)

        return query.all()

    def create(self, title: str, content: str) -> Post:
        new_post = Post(id=str(uuid4()), title=title, content=content)

        self.session.add(new_post)
        self.session.flush()
        return new_post

    def update(self, id: str, title: str, content: str) -> Post:
        post = self.get(id)

        post.title = title
        post.content = content

        self.session.add(post)
        self.session.flush()
        return post

    def delete(self, id: str) -> Post:
        post = self.get(id)

        self.session.delete(post)
        self.session.flush()

        return post
