from uuid import uuid4

from sqlalchemy import Column, Text, String
from sqlalchemy.dialects.postgresql import UUID
from src.datastore.models.base_model import BaseModel
from sqlalchemy.orm import relationship


class Post(BaseModel):
    __tablename__ = "post"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(255))
    content = Column(Text)
