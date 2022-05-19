FROM python:alpine

WORKDIR /usr/app

COPY ./requirements.txt ./
COPY ./ ./

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /usr/app
USER appuser

CMD [ "python", "main.py" ]

