from sqlalchemy import Column, DateTime, inspect
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from src.datastore.func import utcnow

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, server_default=utcnow(), nullable=False)
    updated_at = Column(
        DateTime, server_default=utcnow(), onupdate=utcnow(), nullable=False
    )
