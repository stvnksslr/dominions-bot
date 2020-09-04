# build stage
FROM python:3.8.5-slim-buster as build

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY ./src /app
COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry && \
    python -m poetry install --no-dev

CMD ["slack-machine"]