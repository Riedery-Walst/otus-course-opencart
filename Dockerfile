FROM python:3.12-slim

WORKDIR /tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && \
    apt-get install -y firefox-esr chromium curl && \
    rm -rf /var/lib/apt/lists/*
