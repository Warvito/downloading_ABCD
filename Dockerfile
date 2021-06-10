FROM python:3.9-slim-buster

RUN python -m pip install --upgrade pip
RUN pip3 install nda-tools
