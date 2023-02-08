FROM python:3.9

RUN mkdir /app

WORKDIR /app

ADD . /app/

ENV TZ Europe/Moscow
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

ENV VENV=/app/venv
ENV VENV_ACTIVATE="$VENV/bin/activate"

RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    python3-setuptools \
    python3-pip \
    python3-dev \
    python3-venv \
    git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv $VENV

RUN . $VENV_ACTIVATE && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD . $VENV_ACTIVATE && python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver $HOST:$PORT --noreload
