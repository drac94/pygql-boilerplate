#!/bin/sh

# Usage: runs tests

PIPENV_DOTENV_LOCATION=./.env.test pipenv run pytest
exit "${?}"