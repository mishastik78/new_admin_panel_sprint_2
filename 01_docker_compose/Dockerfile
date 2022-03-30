FROM python:3.10
WORKDIR /code
COPY ./app .
RUN pip install -r requirements.txt
CMD gunicorn docker_test.wsgi:application --bind 0.0.0.0:8000
