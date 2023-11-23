FROM python:3.9.7-slim as base

EXPOSE 8000

WORKDIR /app
COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt
COPY . /app/
COPY entrypoint.sh /entrypoint.sh


FROM postgres:latest as postgres_migration

RUN apt-get update && apt install -y python3 python3-pip python3.11-venv libpq-dev && apt-get clean
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip3 install SQLAlchemy==2.0.23 alembic==1.12.1 psycopg2-binary==2.9.9

WORKDIR /migrations
COPY src/db /migrations
