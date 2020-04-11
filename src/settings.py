from os import environ

# -------------------------
# Core application settings
# -------------------------

# Application environment, should be one of production, staging, development or test
ENVIRONMENT = environ.get("ENVIRONMENT", "development")
# Application log level as defined by Python's logging system
LOG_LEVEL = environ.get("LOG_LEVEL", "DEBUG")

# PostgreSQL
POSTGRES_USER = environ.get("POSTGRES_USER", "")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", "")
POSTGRES_HOST = environ.get("POSTGRES_HOST", "")
POSTGRES_DB = environ.get("POSTGRES_DB", "")
