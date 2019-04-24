FROM python:3.6
RUN apt-get update && apt-get install -y
RUN pip install Flask
RUN useradd -ms /bin/bash/ microservice
USER microservice
WORKDIR /app
COPY app /app
CMD [ "python", "app.py" ]