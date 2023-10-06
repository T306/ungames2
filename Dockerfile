# syntax=docker/dockerfile:1

FROM python:3.12-rc-slim-bookworm
LABEL authors="T306Dev"

EXPOSE 81
WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN python dbgen.py
CMD [ "hypercorn", "main:app"]