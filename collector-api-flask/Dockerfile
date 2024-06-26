# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine AS builder

WORKDIR /src
COPY app/requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY app/ ./

FROM builder as app

CMD ["python3", "server.py"]
