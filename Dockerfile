# syntax=docker/dockerfile:1

FROM python:3.13.5-rc-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

LABEL authors="T306Dev"

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

ADD . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

RUN ["chmod", "+x", "/ungames2/entrypoint.sh"]
CMD [ "./entrypoint.sh"]