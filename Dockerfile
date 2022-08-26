FROM python:3.8

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp
RUN pip3 instlall --upgrade pip && pip3 instlall -r /tmp/requirements.txt && /tmp/requirements.txt

WORKDIR /code
COPY . /code