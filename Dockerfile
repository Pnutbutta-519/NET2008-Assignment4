# syntax=docker/dockerfile:1

FROM python:3

ADD alexvohsemer_assignment4.py /

RUN pip3 install requests

CMD [ "python3", "./alexvohsemer_assignment4.py"]