#!/bin/sh

# Usage: runs tests

COVERAGE_OPTIONS="--cov-report html --cov-report term-missing:skip-covered --cov=src --cov-fail-under=85"
RUN_TEST="PIPENV_DOTENV_LOCATION=./.env.test pipenv run pytest ${COVERAGE_OPTIONS} ${@}"
RUN="${RUN_TEST}"

eval $RUN

exit "${?}"