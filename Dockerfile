# syntax=docker/dockerfile:1

FROM python:3

ADD app.py /

RUN pip3 install requests

CMD [ "python3", "./app.py"]