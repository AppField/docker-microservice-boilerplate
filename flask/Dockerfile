FROM python:3.7-alpine as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY ./app /usr/src/app

WORKDIR /usr/src/app

RUN adduser -D microservice
USER microservice

CMD ["python", "api.py"]

