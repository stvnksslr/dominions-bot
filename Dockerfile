# build stage
FROM python:3.8.3-slim-buster as build

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

COPY ./src /app
COPY pyproject.toml poetry.lock /app/


RUN pip install --no-cache-dir  poetry
RUN python -m poetry config virtualenvs.create false
RUN python -m poetry install --no-dev

CMD ["slack-machine"]