FROM python:3.9.7-slim-bullseye

WORKDIR /app

COPY .env .env
COPY requirements.txt requirements.txt
COPY ./d2d ./d2d

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
