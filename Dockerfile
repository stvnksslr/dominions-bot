# build stage
FROM python:3.8.3-slim-buster as build

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

COPY ./src /app
COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

CMD ["slack-machine"]