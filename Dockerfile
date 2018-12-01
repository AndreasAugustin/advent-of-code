FROM python:3.7.0-alpine3.7

# alpine-sdk needed for clouds-aws (gcc standard libs,..)
RUN apk add --update --no-cache bash make tmux

WORKDIR /app

COPY . /app/
