FROM python:3.10.11-slim-buster

WORKDIR /backend

ENV PYTHONUNBUFFERED 1

RUN apt update && \
    pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system

COPY src .

WORKDIR /backend/src
