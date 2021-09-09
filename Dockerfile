FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
copy ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app