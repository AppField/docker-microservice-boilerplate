FROM python:latest

RUN apt-get update && apt-get install -y
RUN pip install Flask
RUN pip install flask-restful

RUN useradd -ms /bin/bash/ microservice

USER microservice

COPY ./app /usr/src/app

WORKDIR /usr/src/app



CMD ["python", "api.py"]

