# syntax=docker/dockerfile:1

FROM python:3.12-rc-slim-bookworm
LABEL authors="T306Dev"

EXPOSE 81
WORKDIR /ungames2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
USER root
RUN ["chmod", "+x", "/ungames2/entrypoint.sh"]
CMD [ "./entrypoint.sh"]