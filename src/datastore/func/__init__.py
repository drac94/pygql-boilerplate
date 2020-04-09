"""Server functions to use with SQLAlchemy"""
from typing import Any, Dict

from sqlalchemy import DateTime
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression


# To make sure the server is using UTC times regardless of the server configuration.
# See https://docs.sqlalchemy.org/en/13/core/compiler.html#utc-timestamp-function
class utcnow(expression.FunctionElement):
    type = DateTime()


@compiles(utcnow, "postgresql")
def pg_utcnow(element: Any, compiler: Any, **kw: Dict[str, Any]) -> str:
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


__all__ = ("utcnow",)
