from src import settings

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{0}@{1}/{2}".format(
    settings.POSTGRES_USER, settings.POSTGRES_HOST, settings.POSTGRES_DB
)

__all__ = ("SQLALCHEMY_DATABASE_URI",)
