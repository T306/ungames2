# syntax=docker/dockerfile:1

FROM python:3.13.5-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

LABEL org.opencontainers.image.authors="T306"

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

ADD . /app
RUN ["mkdir", "/app/Games"]

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

EXPOSE 5000
#RUN ["chmod", "+x", "/app/entrypoint.sh"]
#CMD [ "./entrypoint.sh"]

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]