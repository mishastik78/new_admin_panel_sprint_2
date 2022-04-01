FROM python:3.10.4-slim-buster
WORKDIR /code
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt
COPY ./app .
CMD gunicorn --workers=2 config.wsgi:application --bind 0.0.0.0:8000
